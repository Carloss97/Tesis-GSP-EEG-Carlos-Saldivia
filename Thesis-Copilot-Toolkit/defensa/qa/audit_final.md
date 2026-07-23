# Auditoría final reproducible

Resultado: **16/16 gates aprobados**.

| Gate | Estado | Evidencia |
|---|---|---|
| `artefactos_requeridos` | APROBADO | faltantes=[] |
| `paginas_presentacion` | APROBADO | páginas=39; esperado=39 |
| `paginas_narrativa` | APROBADO | páginas=16; esperado>=15 |
| `estructura_slides` | APROBADO | principales=25; respaldos=14 |
| `banco_jurado` | APROBADO | preguntas=38 |
| `guion_por_slide` | APROBADO | entradas=25 |
| `tiempo_principal` | APROBADO | total=29:00; acumulado=1740s |
| `rutas_abreviadas` | APROBADO | rutas declaradas=25:00 y 20:00 |
| `terminos_prohibidos` | APROBADO | fuentes=0; pdf=0 |
| `departamento_portada` | APROBADO | texto extraído de la portada |
| `cifras_clave` | APROBADO | ausentes=[] |
| `contenido_cientifico_minimo` | APROBADO | {'exploración': True, 'congelado': True, 'pareado': True, 'limitaciones': True, 'P1': True, 'P2': True} |
| `logs_latex` | APROBADO | {'presentacion_defensa': 0, 'narrativa_defensa': 0} |
| `checksums_figuras` | APROBADO | entradas=12; fallas=[] |
| `render_presentacion` | APROBADO | renderizadas=39; sospechosas=[] |
| `render_narrativa` | APROBADO | renderizadas=16; sospechosas=[] |

## Revisión visual

Se renderizaron y revisaron las 39 páginas de la presentación y todas las páginas de la narrativa. Las hojas de contacto finales están en `previews/presentacion/contact-sheet.png` y `previews/narrativa/contact-sheet.png`. No se observaron recortes, solapamientos, páginas vacías ni contenido fuera del marco.

## Alcance

La auditoría valida estructura, compilación, texto extraído, cifras centrales, checksums y maquetación visible. No convierte los intervalos descriptivos en inferencia poblacional ni amplía el alcance científico declarado en la tesis.
