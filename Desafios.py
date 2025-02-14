    ## DESAFIO 10 ##

# lista = ['a','b','c','d','e']

# lista_novo = list(map(lambda i: print(f'Eu gosto de {i}'), lista))

# print(lista_novo)


    ## DESAFIO 11 ##
 
# for i in range(1,11):
#     print(i)


    ## DESAFIO 12 ##

# frutas = ['Maçã','Banana','Abacate','Laranja','Melancia']
# vegetais = ['Pepino','Abóbora','Xuxu','Cebola','Cenoura']

# for fruta in frutas:
#     for vegetal in vegetais:
#         print(fruta,vegetal)


    ## DESAFIO 13 ##

# numero = 0

# while numero <= 10:
#     print(numero)
#     numero += 1
#     continue


    ## DESAFIO 14 ##

# numero = 1

# while numero <= 10:
#     print(numero)
#     if numero == 5:
#         break
#     numero += 1
#     continue

# print()

# numero = 1

# while numero <= 10:
#     print(numero)
#     numero += 1
#     if numero == 5:
#         numero += 1
#         continue


    ## DESAFIO 15 ##

# frutas = ['Maçã','Maçã','Maçã','Banana','Abacate','Abacaxi']

# contagem = 0

# for nome in frutas:
#     if nome == 'Maçã':
#         contagem += 1

# print(f'Número de maçãs na lista: {contagem}')


    ## DESAFIO 16 ##

# numero = int(input('Digite um número: '))

# if numero > 10:
#     print('O número é maior que 10!')
# else:
#     print('O número é menor ou igual a 10!')


    ## DESAFIO 17 ##

# idade_input = int(input('Digite a sua idade: '))

# if idade_input < 13:
#     print('Você é uma criança!')
# elif idade_input >= 13 and idade_input < 19:
#     print('Você é um adolescente!')
# else:
#     print('Você é um adulto!')


    ## DESAFIO 18 ##

# estoque = ['BMW X6','BMW i5','BMW i8']

# procura = input('Digite o nome de um carro: ')

# if procura in estoque:
#     print('Este carro está disponível!')
# else: 
#     print('Desculpe, este carro não está disponível!')


    ## DESAFIO 19 ##

# import os

# fruta = 'parapapapapapapapapapa'
# while True:
#     tentativa = input('Digite o nome de uma fruta: ').lower()

#     if tentativa != fruta:
#         os.system('cls')
#         continue
#     else:
#         os.system('cls')
#         print(f'Parabéns, você acertou a fruta "{fruta.upper()}"')
#         break


    ## DESAFIO 20 ##

# lista_numeros = list(range(1,101))

# for numero in lista_numeros:
#     if numero % 2 == 0:
#         print(f'O número {numero} é par!')
#         continue
#     else:
#         print(f'O número {numero} é ímpar!')


    ## DESAFIO 21 ##

# lista_cidades = 'Rio de Janeiro','São Paulo','Brasília'

# cidade_input = input('Digite o nome de uma cidade: ')

# if cidade_input in lista_cidades:
#      print('A cidade está na lista de cidades! ')
# else:
#     print('A cidade não está na lista de cidades! ')


    ## DESAFIO 22 ##

# cidades = {
#     'Brasil' : 'Brasília',
#     'Estados Unidos' : 'Washington',
#     'Venezuela' : 'Caracas',
#     'México' : 'México city',
#     'Argentina' : 'Uruguay' 
# }

# pais_input = input('Digite o nome de um país: ')

# if pais_input in cidades:
#     print(f'A capital de {pais_input} é {cidades[pais_input]} ')