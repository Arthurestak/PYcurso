lista = [(1,2), {'nome':'Arthur'}, 1, 3, {1,2,3}]

for i in lista:
    if isinstance(i, int):
        print(f'{i} é um inteiro!\n')
    elif isinstance(i, str):
        print(f'{i} é uma string!\n')
    elif isinstance(i, set):
        i.add('Eu sou um set')
        print(f'{i} é um set!\n')
    else:
        print(f'{i} é outro tipo!\n')

