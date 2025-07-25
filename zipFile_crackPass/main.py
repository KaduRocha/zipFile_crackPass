import os
import zipfile
import rarfile
import py7zr
import glob
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from pathlib import Path

# ---------------------------
# Gera arquivo de senhas numéricas (ex: 000000 a 999999)
# ---------------------------
def gerar_arquivo():
    qt = int(input("Quantidade de dígitos da senha (ex: 6 para 000000 a 999999): "))
    max_val = int('9' * qt)
    with open("pass.txt", "w") as arquivo:
        for num in range(0, max_val):
            arquivo.write(str(num).zfill(qt) + "\n")
    print(f"✔️  Arquivo 'pass.txt' com {max_val} senhas gerado com sucesso.")


# ---------------------------
# Função que cada processo executa
# ---------------------------
def tentar_senha(args):
    arquivo, senha, tipo = args
    try:
        if tipo == 'zip':
            with zipfile.ZipFile(arquivo) as zf:
                zf.extractall(pwd=senha)
        elif tipo == 'rar':
            with rarfile.RarFile(arquivo) as rf:
                rf.extractall(pwd=senha.decode())
        elif tipo == '7z':
            with py7zr.SevenZipFile(arquivo, mode='r', password=senha.decode()) as sz:
                sz.extractall()
        else:
            return None
        return senha.decode()
    except:
        return None

# ---------------------------
# Detectar tipo de arquivo
# ---------------------------
def detectar_tipo(arquivo):
    ext = os.path.splitext(arquivo)[1].lower()
    if ext == '.zip':
        return 'zip'
    elif ext == '.rar':
        return 'rar'
    elif ext == '.7z':
        return '7z'
    else:
        return None

# ---------------------------
# Função principal com multiprocessing + tqdm
# ---------------------------
def crack_multicore(arquivo, pass_file):
    if not os.path.exists(arquivo):
        print(f"❌  Arquivo compactado '{arquivo}' não encontrado!")
        return

    tipo = detectar_tipo(arquivo)
    if not tipo:
        print(f"❌  Tipo de arquivo não suportado: {arquivo}")
        return

    if not os.path.exists(pass_file):
        print("❌  Arquivo de senhas não encontrado!")
        return

    with open(pass_file, 'rb') as f:
        senhas = [line.strip() for line in f if line.strip()]

    total = len(senhas)
    print(f"\n📂  Arquivo: {arquivo}")
    print(f"📦  Tipo detectado: {tipo.upper()}")
    print(f"🔢  Total de senhas a testar: {total}")
    print(f"⚙️  Usando {cpu_count()} núcleos...\n")

    args = [(arquivo, senha, tipo) for senha in senhas]

    with Pool(cpu_count()) as pool:
        for result in tqdm(pool.imap_unordered(tentar_senha, args), total=total, desc="Tentando senhas", unit=" tentativa"):
            if result:
                print(f"\n✅  SENHA ENCONTRADA para '{arquivo}': {result}")
                pool.terminate()
                return result

    print(f"\n❌  Nenhuma senha encontrada para '{arquivo}'.")
    return None

# ---------------------------
# Execução principal
# ---------------------------
if __name__ == "__main__":
    # Etapa 1: gerar lista de senhas
    gerar_arquivo()
    pass_file = "pass.txt"

    # Define extensões desejadas
    extensoes = ['.zip', '.rar', '.7z', '.tar']

    # Etapa 2: tentar quebrar o ZIP.
    # Pega todos os arquivos na pasta target referente as extensoes suportadas.
    arquivos = [str(f) for f in Path("target").glob("*") if f.suffix.lower() in extensoes]
    if not arquivos:
        print("❌  Nenhum arquivo encontrado na pasta 'target'.")
    else:
        for arquivo in arquivos:
            if detectar_tipo(arquivo):
                crack_multicore(arquivo, pass_file)
            else:
                print(f"⏩  Ignorando '{arquivo}' (formato não suportado)")