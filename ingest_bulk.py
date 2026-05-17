import os
import glob
import re
from datetime import datetime

raw_dir = 'raw'
wiki_dir = 'wiki'
index_file = os.path.join(wiki_dir, 'index.md')
log_file = os.path.join(wiki_dir, 'log.md')

files = glob.glob(os.path.join(raw_dir, '*.md'))
already_processed = [
    'Explicação.md',
    'Detecção de Objetos Usando YOLO e Python.md',
    'Projeto de Sistemas Multiagentes _ Geração de relatório a partir de Dados de rastreamento..md',
    'Reconhecimento de objectos com Yolo e OpenCV - AranaCorp.md',
    'README.md',
    'Just a moment....md'
]

def get_category(content):
    c = content.lower()
    if 'yolo' in c or 'vision' in c or 'visão' in c or 'opencv' in c: return 'Visão Computacional'
    if 'quantum' in c or 'quântic' in c: return 'Computação Quântica'
    if 'bioinformatic' in c or 'biotech' in c: return 'Bioinformática e Biotech'
    if 'skill' in c or 'agent' in c or 'claude' in c or 'gemini' in c: return 'Agent Skills'
    if 'job' in c or 'career' in c or 'talent' in c or 'trend' in c or 'labor' in c: return 'Carreiras e Tendências'
    if 'cybersecurity' in c or 'security' in c: return 'Cibersegurança'
    return 'Geral'

log_entries = []
index_entries = {'Visão Computacional': [], 'Computação Quântica': [], 'Bioinformática e Biotech': [], 'Agent Skills': [], 'Carreiras e Tendências': [], 'Cibersegurança': [], 'Geral': []}

for f in files:
    filename = os.path.basename(f)
    if filename in already_processed: continue
    
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filename.replace('.md', '')
    
    # safe filename
    safe_title = re.sub(r'[^\w\-_\. ]', '_', title)[:100]
    out_file = os.path.join(wiki_dir, f'{safe_title}.md')
    
    category = get_category(content)
    
    # get first non-empty text paragraph
    lines = content.split('\n')
    summary = 'Documento sem resumo automático.'
    for line in lines:
        if line.strip() and not line.startswith('#') and not line.startswith('---') and not line.startswith('sourceFile:') and not line.startswith('exportDate:') and 'http' not in line:
            if len(line) > 30:
                summary = line[:200] + '...' if len(line) > 200 else line
                break
                
    wiki_content = f"""---
title: {title}
date: {datetime.now().strftime('%Y-%m-%d')}
category: {category}
sources: [{f.replace('\\', '/')}]
---

# {title}

**Categoria:** {category}

## Resumo Automático
{summary}

*Este arquivo foi gerado por um script de ingestão em massa.*
"""
    with open(out_file, 'w', encoding='utf-8') as fp:
        fp.write(wiki_content)
        
    index_entries[category].append(f'- [{title}]({safe_title}.md)')
    log_entries.append(f'## [{datetime.now().strftime("%Y-%m-%d")}] ingest | {filename}')

# Update index
with open(index_file, 'r', encoding='utf-8') as f:
    idx_content = f.read()

new_idx = []
for cat, entries in index_entries.items():
    if entries:
        new_idx.append(f'### {cat}\n' + '\n'.join(entries) + '\n')

if new_idx:
    idx_content += '\n## Novas Categorias (Ingestão em Massa)\n\n' + '\n'.join(new_idx)
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(idx_content)

# Update log
if log_entries:
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write('\n' + '\n'.join(log_entries) + '\n')

print(f'Processed {len(log_entries)} files.')
