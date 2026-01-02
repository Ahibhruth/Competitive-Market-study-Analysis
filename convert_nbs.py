import json
import os

def notebook_to_script(notebook_path, output_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    script_content = []
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell['source']
            if isinstance(source, list):
                source = ''.join(source)
            
            script_content.append(f"# %% Cell Type: {cell['cell_type']}\n")
            script_content.append(source + "\n\n")
            
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(script_content)
    print(f"Converted {notebook_path} to {output_path}")

notebook_to_script('eda.ipynb', 'reproduce_eda.py')
notebook_to_script('eda copy.ipynb', 'reproduce_eda_copy.py')
