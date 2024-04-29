import os
import zipfile

# Parâmetros iniciais.
fpass = 'pass.txt'
file = 'target\\lmasnflmas.zip'
fzip = zipfile.ZipFile(file)

# Função para preparar arquivo pass.txt
def gerar_arquivo():
    qt = int(input("Quantidade de digitos: "))
    start = 0
    step = 1
    fim = str(9).zfill(qt)
    os.remove("pass.txt")
    arquivo = open("pass.txt", "x")
    gerar_sequencia(start, qt, step)
    
# Função para gerar uma sequência de números inteiros
def gerar_sequencia(start, qt, step):
   arquivo = open("pass.txt", "w")
   while start <= int(999999):
        arquivo.writelines([str(start).zfill(qt),"\n"])
        start += 1

def crackPass(fpass, fzip):
    QTentataivas = 0

    with open(fpass, 'rb') as zfile:
        for line in zfile:
            for pswd in line.split():
                try:
                    QTentataivas += 1
                    fzip.extractall(pwd = pswd)
                    # print('Quantidade de Tentativas: ', QTentataivas)
                    print('A senha é: ', pswd.decode())
                    return True
                except:
                    continue
    return False

gerar_arquivo()
# if gerar_arquivo() == True:
    # print("Arquivo com senhas para teste gerado com sucesso!")

if crackPass(fpass, fzip) == False:
    print('Nao encontrado!')