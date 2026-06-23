# Plan formal — corrección de figuras capítulos 1–3

## 1. Alcance

1. Corregir las figuras observadas por el profesor en capítulos 2 y 3 antes de avanzar con el rediseño del capítulo 4.
2. Trabajar desde los scripts generadores y regenerar PDFs vectoriales; no editar manualmente los PDFs.
3. Mantener las figuras como esquemas propios basados en las referencias citadas, evitando copiar imágenes de artículos salvo que exista autorización/licencia clara.
4. Verificar en PDF compilado y con QA visual antes de dar por cerrado.

## 2. Checklist por figura

### Figura 2.1 — Generación EEG / ERP / topografía

1. Reducir espacio en blanco alrededor de la figura.
2. Rediseñar panel (a) para que se entienda como cabeza/corteza, no como capas rectangulares abstractas.
3. Mover y aclarar la etiqueta de dipolos corticales.
4. Mejorar panel (b) para conectar campo de dipolo con cabeza/conducción.
5. Mover etiquetas ERP, especialmente P300, para evitar solapes con picos.
6. Mejorar panel (d) con referencia explícita a cabeza: nariz, orejas, contorno y orientación.
7. Mantener la cita en caption como esquema propio basado en Nunez/Srinivasan y Luck.

### Figura 2.2 — Conceptos GSP

1. Rehacer panel (a) como grafo tipo EEG con contorno de cabeza, nariz, orejas y electrodos reconocibles.
2. Evitar que la explicación “nodos/aristas” se sobreponga con el dibujo.
3. Cambiar panel (b) para responder la crítica: separar autovalores del Laplaciano de energía de señal.
4. Mostrar explícitamente que los autovalores aumentan, mientras una curva de energía modal ilustrativa decrece para modos altos.
5. Quitar el subtítulo/frase inferior “La solución conserva...”.
6. Simplificar panel (c) para que sea una formulación visual limpia de reconstrucción regularizada.

### Figura 2.3 — Objetivo TRSS

1. Eliminar subtítulo superior innecesario.
2. Separar bloques y fórmulas para que no haya solapes.
3. Enrutar flechas sin cruzar fórmulas.
4. Centrar cada fórmula con su término.
5. Mantener lectura izquierda→centro→derecha: observaciones → términos → reconstrucción.

### Figura 3.1 — Flujo metodológico

1. Sacar espacio vertical sobrante.
2. Quitar bloque gris inferior.
3. Poner comparación/análisis como paso final horizontal, no como bloque inferior ambiguo.
4. Agrupar métricas por categoría y separar costo computacional.
5. Actualizar caption para que no hable de tests de hipótesis ni “análisis estadístico pareado” como eje.

### Figura 3.2 — Arquitectura modular

1. Sacar espacio vertical sobrante.
2. Quitar barra gris inferior.
3. Renombrar primer bloque a “Datos EEG”.
4. Corregir MNE Sample como 60 canales EEG y no 8 canales.
5. Representar separación exploratoria/comparativa mediante etiquetas claras, no nota gris pequeña.
6. Simplificar texto interno para mejorar legibilidad.

### Figura 3.3 — Trazabilidad

1. Quitar nota inferior redundante y bloque gris pequeño.
2. Clarificar “Documento de tesis” como salida final.
3. Evitar duplicar el caption dentro de la imagen.
4. Aumentar legibilidad y evitar flechas cruzando texto.

## 3. Verificación requerida

1. Regenerar figuras con Python en entorno virtual temporal.
2. Compilar `tesis_completa.tex`.
3. Compilar `tesis_caps_1_5.tex` si sigue presente.
4. Ejecutar `scripts/validate_thesis.py`.
5. Revisar conteo de errores/citas/referencias/overfull hbox.
6. Generar contact sheets de QA visual y revisarlas.
