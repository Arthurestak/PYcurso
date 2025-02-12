condicao = True

while condicao:
    nome = input ('Qual é o seu nome: ')
    print (f'Seu nome é {nome}')
    if nome == 'sair':
        print('Você escolheu sair!')
        break
# contador = 0

# while contador < 10:
#     contador = contador + 1
#     print (contador)
# print('Acabou!')


contador = 10

while contador <= 1000:  
    contador += 1
    print (contador)
