# Revisión final tipo profesor guía — Capítulos 4, 5 y 6

Fecha: 2026-07-07  
Contexto: pasada final después de corregir metadata/portada, eliminar menciones a Visibility/NNK y reemplazar tablas densas de Capítulo 6 por prosa/listas.

## 1. Comentario general

El documento está mucho más defendible que las versiones previas porque ya no presenta el Capítulo 4 como un bloque de resultados aislados. La estructura actual permite seguir la lógica experimental: exploración preliminar, reducción de candidatos, optimización intermedia, comparación final y frontera práctica. Esta organización es adecuada para una tesis de magíster porque muestra el proceso de decisión, no solo el resultado más favorable.

## 2. Capítulo 4 — Experimentos y Resultados

### Fortalezas

- La separación entre evidencia preliminar y evidencia final está clara.
- La Tabla 4.1 ya no queda como ranking final, sino como justificación de reducción del espacio experimental.
- La Figura 4.1 aporta una síntesis visual útil de la campaña exploratoria y evita depender solo de tablas.
- La Tabla 4.2 resolvió el problema de columna duplicada: ahora el lector entiende el rol experimental de cada método.
- La comparación TRSS--MNE está formulada como evidencia descriptiva pareada, no como una afirmación absoluta.
- La sección de frontera práctica es uno de los cierres más fuertes del capítulo: entrega una regla de uso defendible.

### Riesgos revisados

- Riesgo de mencionar métodos no usados finalmente: corregido. Se eliminaron menciones a Visibility/NNK del documento activo.
- Riesgo de que la selección preliminar parezca prueba final: controlado mediante texto explícito y separación de fases.
- Riesgo de sobrecargar con tablas conceptuales: mitigado por versiones previas al mover varias tablas textuales a prosa.

### Corrección aplicada en esta pasada

- Se cambió “TV dirigida” por “TV temporal” para alinear mejor la frase con la nomenclatura visible y evitar confusión.
- Se eliminó cualquier mención textual a Visibility/NNK en Capítulo 4.

## 3. Capítulo 5 — Discusión

### Fortalezas

- La discusión ahora interpreta la trayectoria experimental completa, no solo el resultado final.
- MNE-Python queda correctamente tratado como referencia fuerte, no como baseline débil.
- TRSS se presenta de manera condicional y defendible: útil en pérdida espacial difícil, no dominante universalmente.
- Las limitaciones están formuladas de forma honesta: canales artificialmente ocultos, ausencia de evaluación experta y falta de tareas posteriores.

### Comentario crítico

El capítulo es sólido y coherente con Capítulo 4. La sección de métodos no finalistas ayuda a justificar que la tesis implementó más que TRSS/MNE, pero no debería crecer más: si se agregan nuevas frases, puede volver a parecer una revisión de métodos en vez de una discusión. Mantenerlo como está.

### Corrección aplicada en esta pasada

- Se eliminó el párrafo que mencionaba explícitamente Visibility/NNK. La discusión conserva la idea metodológica de trazabilidad sin nombrar un método descartado que no aporta al cierre.

## 4. Capítulo 6 — Conclusiones y Trabajo Futuro

### Fortalezas

- Las preguntas P1/P2 se responden directamente.
- La conclusión evita una declaración de superioridad universal.
- El trabajo futuro está priorizado en líneas técnica, experimental, metodológica y de extensión.
- El cierre final es preciso: MNE como referencia robusta y rápida; TRSS como alternativa justificable en pérdida espacial difícil con costo aceptable.

### Problema detectado

Las tablas internas del Capítulo 6 comprimían demasiado texto y hacían que el cierre se viera más estrecho de lo necesario. Para un capítulo de conclusiones, una tabla densa rompe el ritmo y transmite una sensación de checklist administrativo.

### Corrección aplicada

- Se eliminó la tabla de fases del cuerpo del Capítulo 6 y se reemplazó por un resumen narrativo en cuatro decisiones.
- Se eliminó la matriz de cumplimiento del cuerpo del Capítulo 6 y se reemplazó por una lista breve de cumplimiento de objetivo general, OE1, OE2, OE3, P1 y P2.
- Las tablas descriptivas extensas permanecen como soporte en anexos, no como carga visual del cierre.

## 5. Metadata y portada

Comentario del profesor resuelto:

- `Departamento de Ingeniería Electrónica` pasó a `Departamento de Electrónica`.
- La corrección se hizo tanto en `config/metadata.tex` como en `frontmatter/cover_page.tex`, porque la portada no dependía completamente del macro de metadata.

## 6. Revisión de lenguaje y consistencia

- No quedan menciones activas a Visibility/NNK en capítulos, anexos, tablas, metadata o portada.
- No queda lenguaje de `cribado`, `Wilcoxon`, `q_{BH}`, `significancia`, `H1`, `H2`, `benchmark final` o `ablación` en fuentes activas del documento.
- No quedan rutas locales ni nombres de archivo tipo `.fif` en capítulos/anexos/tablas activos.
- El documento mantiene el marco de preguntas de investigación, comparación pareada descriptiva y frontera práctica.

## 7. Observación final de profesor guía

El manuscrito ya tiene una línea argumental defendible: no promete que TRSS sea universalmente mejor, sino que muestra cuándo su regularización temporal aporta valor frente a una referencia madura. Ese matiz es importante para defensa. Las correcciones más relevantes ahora son de presentación y cierre, no de fondo: evitar tablas densas en conclusiones, no mencionar métodos descartados que no aportan al relato final y mantener cada conclusión conectada con evidencia trazable del Capítulo 4.
