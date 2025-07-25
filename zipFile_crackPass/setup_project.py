import os

# project_name = 'ZIPFILE_CRACKPASS'
folders = [
      'files'
    , 'files/input'
    , 'files/output'
]

# Cria estrutura
for folder in folders:
    os.makedirs(os.path.join(folder), exist_ok=True)

# Cria README.md
with open(os.path.join('README.md'), 'w', encoding='utf-8') as f:
    f.write('# Projeto quebrar senhas de arquivos compactados [.zip, .rar e .7z].\n\n' \
    'Passo 1 - Executar o setup_project.py para criar estrutura de pastas.\n'
    'Passo 2 - Após a execução do setup_project.py, coloque o arquivo que pretende descompactar na pasta files/input.\n'
    'Passo 3 - Após concluido os passos anteriores, executar o programa através do arquivo main.py')

# Cria requirements.txt
with open(os.path.join('requirements.txt'), 'w') as f:
    f.write('os\nzipfile\nrarfile\npy7zr\nglob\ntqdm\nmultiprocessing\npathlib')

print(f'✅  Estrutura criada com sucesso!')
