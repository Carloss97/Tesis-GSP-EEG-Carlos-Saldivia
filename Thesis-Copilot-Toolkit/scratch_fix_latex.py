import glob
import os

for filepath in glob.glob('thesis/usm/chapters/*.tex'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix double backslashes
    content = content.replace(r'\\\\', '\\')
    
    # Fix quotes issue for babel-spanish
    # Let's just replace "cruce de rendimiento" with ``cruce de rendimiento''
    content = content.replace('"cruce de rendimiento"', "``cruce de rendimiento''")
    content = content.replace('"señal sobre el grafo"', "``señal sobre el grafo''")
    content = content.replace('"forma"', "``forma''")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
