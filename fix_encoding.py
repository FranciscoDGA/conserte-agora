import os
import glob

# Mapeamento dos caracteres corrompidos
fixes = {
    'Ã£': 'ã',
    'Ã§': 'ç',
    'Ã©': 'é',
    'Ã­': 'í',
    'Ã³': 'ó',
    'Ãº': 'ú',
    'Ã¢': 'â',
    'Ãª': 'ê',
    'Ãµ': 'õ',
    'Ã¡': 'á',
    'Ã ': 'À',
    'Ã§Ã£o': 'ção',
    'Ã§Ãµes': 'ções',
}

files = glob.glob('**/*.html', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    modified = False
    for bad, good in fixes.items():
        if bad in content:
            content = content.replace(bad, good)
            modified = True
            
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Codificação corrigida.")
