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
    'Passo 1 - Executar o GIT CLONE com o seguinte comando: https://github.com/KaduRocha/zipFile_crackPass.git\n'
    'Passo 2 - Executar o setup_project.py para criar estrutura de pastas. Execute o seguinte comando: python setup_project.py\n'
    'Passo 3 - Executar o requeriments.txt para instalar as libs necessarias. Execute o seguinte comando: pip install -r requirements.txt\n'
    'Passo 4 - Após a execução do setup_project.py, coloque o arquivo que pretende descompactar na pasta files/input.\n'
    'Passo 5 - Após concluido os passos anteriores, executar o programa através do arquivo main.py com o seguinte comando: Python main.py')

# Cria requirements.txt
with open(os.path.join('requirements.txt'), 'w') as f:
    f.write('rarfile\npy7zr\ntqdm\npathlib')

print(f'✅  Estrutura criada com sucesso!')
