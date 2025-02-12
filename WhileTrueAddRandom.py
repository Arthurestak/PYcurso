import random as rd 

lista = []
while True:
    add = input('Deseja adicionar um número aleatório na lista? [s][n]')

    if add.startswith('s'):
        lista.append(rd.choice(range(1,100)))
    else:
        break
    continue
lista.insert(0, 999)
print(lista)
