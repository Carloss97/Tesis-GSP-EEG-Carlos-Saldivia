import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob
import os

def load_all_iterations(results_dir):
    """Busca y concatena todos los archivos itX*_raw.csv o itX*_stats.csv en el directorio."""
    # Buscar archivos crudos de iteraciones
    files = glob.glob(os.path.join(results_dir, "itX*_raw.csv"))
    
    if not files:
        print(f"No se encontraron archivos crudos. Buscando stats...")
        files = glob.glob(os.path.join(results_dir, "itX*_stats.csv"))
        
    if not files:
        print("No se encontraron archivos de iteraciones en el directorio. Generando dummy data.")
        return simulate_dummy_data()
        
    print(f"Cargando {len(files)} archivos de iteraciones desde {results_dir}...")
    df_list = [pd.read_csv(f) for f in files]
    df_concat = pd.concat(df_list, ignore_index=True)
    
    # Estandarizar nombres de columnas (Mapeo a mayúsculas como espera el script)
    col_map = {
        'mae': 'MAE', 'rmse': 'RMSE', 'dtw': 'DTW', 'snr': 'SNR',
        'method_family': 'Familia', 'family': 'Familia', 
        'method': 'Metodo', 'missing_level': 'Missing_Level',
        'dataset': 'Dataset', 'graph': 'Grafo', 'graph_method': 'Grafo'
    }
    df_concat.rename(columns=lambda x: col_map.get(x.lower(), x), inplace=True)
    
    # Heurística para crear 'Familia' si no existe explícitamente pero sí 'Metodo'
    if 'Familia' not in df_concat.columns and 'Metodo' in df_concat.columns:
        df_concat['Familia'] = df_concat['Metodo'].apply(
            lambda x: 'Baseline' if 'spline' in str(x).lower() else ('TV/Tiempo' if 'trss' in str(x).lower() else 'GSP Instantáneo')
        )
        
    # Asegurar existencia de columnas para la combinación
    for col in ['Dataset', 'Grafo', 'Metodo']:
        if col not in df_concat.columns:
            df_concat[col] = 'N/A'
            
    df_concat['Dataset'] = df_concat['Dataset'].fillna('N/A')
    df_concat['Grafo'] = df_concat['Grafo'].fillna('N/A')
    df_concat['Metodo'] = df_concat['Metodo'].fillna('N/A')
    
    # Crear columna de combinación unificada
    df_concat['Combinacion'] = df_concat['Dataset'].astype(str) + " | " + df_concat['Grafo'].astype(str) + " | " + df_concat['Metodo'].astype(str)
        
    return df_concat

def generate_metric_plots(results_dir="results", output_dir="results/plots"):
    """
    Genera gráficos comparativos por dataset para MAE, RMSE, DTW y SNR agrupando todas las iteraciones.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = load_all_iterations(results_dir)
    
    metrics = [m for m in ['MAE', 'RMSE', 'DTW', 'SNR'] if m in df.columns]
    if not metrics:
        print("Las columnas de métricas no se encontraron en los datos cargados.")
        return

    sns.set_theme(style="whitegrid")

    datasets = df['Dataset'].unique()
    print(f"Análisis encontrado para los siguientes datasets: {datasets}")

    for dataset_name in datasets:
        print(f"\n--- Generando gráficos para el dataset: {dataset_name} ---")
        df_dataset = df[df['Dataset'] == dataset_name].copy()

        def filter_extremes(data, col):
            if col not in data.columns or data[col].isnull().all(): return data
            q_low, q_high = data[col].quantile(0.05), data[col].quantile(0.95)
            return data[(data[col] >= q_low) & (data[col] <= q_high)]

        # 1. Gráfico de Barras: Comparación por Familia (Corregido filtrando outliers)
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle(f'Desempeño Promedio por Familia - Dataset: {dataset_name}', fontsize=16)
        
        for idx, metric in enumerate(metrics):
            ax = axes[idx // 2, idx % 2]
            df_metric_filtered = filter_extremes(df_dataset, metric)
            sns.barplot(data=df_metric_filtered, x='Familia', y=metric, ax=ax, capsize=.1, errorbar='sd', palette='viridis')
            ax.set_title(f'Comparación de {metric}')
            if metric in ['MAE', 'RMSE', 'DTW']:
                ax.set_ylabel(f'{metric} (Menor es mejor)')
            else:
                ax.set_ylabel(f'{metric} (Mayor es mejor)')
                
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{dataset_name}_familia_comparison.png", dpi=300)
        plt.close()

        # 2. Boxplots: Análisis de Varianza y Outliers
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        fig.suptitle(f'Análisis de Outliers y Varianza - Dataset: {dataset_name}', fontsize=16)

        df_mae_filtered = filter_extremes(df_dataset, 'MAE')
        sns.boxplot(data=df_mae_filtered, x='Familia', y='MAE', ax=axes[0], palette='Set2')
        axes[0].set_title('Distribución MAE (Estabilidad)')
        
        if 'RMSE' in df_dataset.columns:
            df_rmse_filtered = filter_extremes(df_dataset, 'RMSE')
            sns.boxplot(data=df_rmse_filtered, x='Familia', y='RMSE', ax=axes[1], palette='Set2')
            axes[1].set_title('Distribución RMSE (Sensibilidad)')
        else:
            axes[1].set_title('RMSE no disponible')
        
        if 'SNR' in df_dataset.columns:
            df_snr_filtered = filter_extremes(df_dataset, 'SNR')
            sns.boxplot(data=df_snr_filtered, x='Familia', y='SNR', ax=axes[2], palette='Set2')
            axes[2].set_title('Distribución SNR (Calidad Global)')
        else:
            axes[2].set_title('SNR no disponible')
        
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{dataset_name}_outliers_variance.png", dpi=300)
        plt.close()

        # 3. Gráficos detallados por combinación (Dataset x Grafo x Método)
        unique_combs = df_dataset['Combinacion'].nunique()
        if unique_combs == 0:
            print(f"No hay combinaciones para graficar en el dataset {dataset_name}.")
            continue
            
        fig_height = max(8, unique_combs * 0.4)

        for metric in metrics:
            fig, ax = plt.subplots(figsize=(14, fig_height))
            df_filtered = filter_extremes(df_dataset, metric)
            
            if df_filtered.empty:
                print(f"No hay datos para la métrica {metric} en el dataset {dataset_name} después de filtrar.")
                plt.close()
                continue

            ascending_order = metric in ['MAE', 'RMSE', 'DTW']
            order = df_filtered.groupby('Combinacion')[metric].median().sort_values(ascending=ascending_order).index
            
            sns.boxplot(data=df_filtered, x=metric, y='Combinacion', ax=ax, order=order, palette='tab20', orient='h')
            ax.set_title(f'Distribución de {metric} por Combinación - Dataset: {dataset_name}', fontsize=16)
            ax.set_xlabel(f'{metric} {"(Menor es mejor)" if ascending_order else "(Mayor es mejor)"}')
            ax.set_ylabel('Combinación (Grafo | Método)')
            
            # Limpiar las etiquetas del eje Y para no repetir el dataset
            labels = [item.get_text().replace(f"{dataset_name} | ", "") for item in ax.get_yticklabels()]
            ax.set_yticklabels(labels)
            
            plt.tight_layout()
            plt.savefig(f"{output_dir}/{dataset_name}_combinacion_detallada_{metric.lower()}.png", dpi=300)
            plt.close()

    # Exportar datos resumidos para análisis manual
    print("\nExportando tablas de resumen a CSV...")
    summary_combinaciones = df.groupby(['Dataset', 'Familia', 'Combinacion'])[metrics].median().reset_index()
    summary_combinaciones.to_csv(f"{output_dir}/resumen_combinaciones_mediana.csv", index=False)
    
    summary_familias = df.groupby(['Dataset', 'Familia'])[metrics].agg(['mean', 'median', 'std']).reset_index()
    # Aplanar las columnas MultiIndex para el CSV
    summary_familias.columns = ['_'.join(col).strip('_') for col in summary_familias.columns.values]
    summary_familias.to_csv(f"{output_dir}/resumen_familias_stats.csv", index=False)

    print(f"\nGráficos generados exitosamente en {output_dir}")

def simulate_dummy_data():
    """Genera un DataFrame dummy para probar el script."""
    np.random.seed(42)
    familias = ['Baseline', 'GSP Instantáneo', 'TV/Tiempo']
    datasets = ['MNE', 'PhysioNet']
    data = []
    for ds in datasets:
        for fam in familias:
            for _ in range(25): # 25 per dataset
                if fam == 'Baseline':
                    base_mae = 0.12 if ds == 'MNE' else 0.18
                    data.append([fam, 'Random', 0.2, np.random.normal(base_mae, 0.01), np.random.normal(base_mae + 0.03, 0.02), np.random.normal(4.5, 0.5), np.random.normal(18, 2), ds, 'N/A', 'spherical_spline'])
                elif fam == 'GSP Instantáneo': 
                    base_mae = 0.11 if ds == 'MNE' else 0.17
                    data.append([fam, 'Random', 0.2, np.random.normal(base_mae, 0.03), np.random.normal(base_mae + 0.09, 0.10), np.random.normal(4.3, 0.6), np.random.normal(19, 4), ds, 'knn', 'tikhonov'])
                else: 
                    base_mae = 0.11 if ds == 'MNE' else 0.16
                    data.append([fam, 'Random', 0.2, np.random.normal(base_mae, 0.02), np.random.normal(base_mae + 0.05, 0.05), np.random.normal(2.5, 0.3), np.random.normal(22, 3), ds, 'gaussian', 'trss'])
                
    return pd.DataFrame(data, columns=['Familia', 'Escenario', 'Missing_Level', 'MAE', 'RMSE', 'DTW', 'SNR', 'Dataset', 'Grafo', 'Metodo'])

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Análisis Global de Iteraciones")
    parser.add_argument("--results_dir", type=str, default="../../results", help="Directorio donde están los itX####_raw.csv")
    parser.add_argument("--output_dir", type=str, default="results/plots", help="Directorio de salida para los gráficos")
    args = parser.parse_args()
    
    generate_metric_plots(args.results_dir, args.output_dir)