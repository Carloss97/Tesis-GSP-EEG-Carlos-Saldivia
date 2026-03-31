            # Evaluación de reconstrucción (MAE)
            from src.evaluation.evaluation import evaluate_reconstruction
            print("Evaluando reconstrucción (MAE)...")
            # Para la demo, usamos la señal original como ground truth y la incompleta para saber dónde evaluar
            mae_result = evaluate_reconstruction(data['signals'], signals_reconstructed, metrics=["mae"])
            print(f"MAE reconstrucción (dummy): {mae_result['mae']}")
        # Interpolación/reconstrucción (dummy)
        from src.interpolation.interpolators import interpolate
        print("Interpolando señales (dummy_mean)...")
        interp_result = interpolate("dummy_mean", signals_incomplete, graph['adjacency'])
        signals_reconstructed = interp_result['signals_reconstructed']
        print(f"Señales reconstruidas shape: {signals_reconstructed.shape}")
    # Simulación de canales faltantes
    from src.data.data_loader import simulate_missing_channels
    print("Simulando canales faltantes (10%)...")
    signals_incomplete = simulate_missing_channels(data['signals'], missing_ratio=0.1)
    print(f"Señales con faltantes shape: {signals_incomplete.shape}")
"""
experiment_pipeline.py
Script principal para orquestar el pipeline de experimentos y comparación.
"""

# Ejemplo de estructura general (no implementado)
# 1. Cargar dataset
# 2. Construir grafo
# 3. Simular canales faltantes
# 4. Interpolar/reconstruir
# 5. Evaluar y guardar resultados

if __name__ == "__main__":
    from src.data.data_loader import load_mne_sample_dataset
    from src.graph_construction.graph_constructors import build_graph
    print("Cargando MNE Sample Dataset...")
    data = load_mne_sample_dataset()
    print(f"Señales shape: {data['signals'].shape}")
    print(f"Posiciones shape: {data['positions'].shape}")
    print(f"Info: {data['info']}")

    # Construcción de grafos
    for graph_method, graph_kwargs in [("knn", {"k": 5}), ("gaussian", {"sigma": 1.0})]:
        print(f"\nConstruyendo grafo: {graph_method}...")
        graph = build_graph(graph_method, data['positions'], **graph_kwargs)
        print(f"Grafo info: {graph['info']}")
        print(f"Matriz de adyacencia (shape): {graph['adjacency'].shape}")

        # Simulación de canales faltantes
        from src.data.data_loader import simulate_missing_channels
        print("Simulando canales faltantes (10%)...")
        signals_incomplete = simulate_missing_channels(data['signals'], missing_ratio=0.1)
        print(f"Señales con faltantes shape: {signals_incomplete.shape}")

        # Interpolación/reconstrucción (dummy y laplacian)
        from src.interpolation.interpolators import interpolate
        for interp_method in ["dummy_mean", "laplacian"]:
            print(f"Interpolando señales ({interp_method})...")
            interp_result = interpolate(interp_method, signals_incomplete, graph['adjacency'])
            signals_reconstructed = interp_result['signals_reconstructed']
            print(f"Señales reconstruidas shape: {signals_reconstructed.shape}")

            # Evaluación de reconstrucción (MAE)
            from src.evaluation.evaluation import evaluate_reconstruction
            print("Evaluando reconstrucción (MAE)...")
            mae_result = evaluate_reconstruction(data['signals'], signals_reconstructed, metrics=["mae"])
            print(f"MAE reconstrucción ({graph_method}, {interp_method}): {mae_result['mae']}")
