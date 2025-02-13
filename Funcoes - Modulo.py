def somar(x,y):
    try:
        x = int(x)
        y = int(y)

        print(x + y)
    except:
        print('Não foi possível transformar o que foi digitado em número! ')

def achar_index(item, lista):
    for i, valor in enumerate(lista):
        if valor in item:
            print(f'O item {item.upper()}, está no índice {i}!')
