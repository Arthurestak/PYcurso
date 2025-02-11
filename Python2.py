import os

linhas = int(input('Quantas linhas você deseja: '))
colunas = int(input('Quantas colunas você deseja: '))
simbolo = input('Qual símbolo você deseja: ')
os.system('cls')
print(f'Aqui está: \nLinhas: {linhas}, Colunas: {colunas}\n')
for i in range(linhas):
    for i2 in range(colunas):
        print(simbolo, end='')
    print()