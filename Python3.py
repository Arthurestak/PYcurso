import os

print('Seja bem-vindo(a) à sua calculadora!\n')

nums = []

def sum(*numeros):
    resultado = 0
    for i in numeros:
        iInt = int(i)
        resultado += iInt
def multi(*numeros):
    resultado = 0
    for i in numeros:
        iInt = int(i)
        resultado *= iInt
def div(*numeros):
    resultado = 0
    for i in numeros:
        iInt = int(i)
        resultado /= iInt
def subs(*numeros):
    resultado = 0
    for i in numeros:
        iInt = int(i)
        resultado -= iInt

calculo = input('Digite a operação que você deseja executar: (X,/,+,-) ').lower()
while True:
    numero = int(input('Digite um número: '))
    nums.append(numero)
    again = input('Deseja digitar outro numero? [S] [N] ').lower()

    if again.startswith('s'):
        os.system('cls')
        continue
    else:
        resultado = 0

        if calculo == '+':
            sum(nums)
            print(resultado)
        elif calculo == '/':
            div(nums)
            print(resultado)
        elif calculo == 'x':
            multi(nums)
            print(resultado)
        elif calculo == '-':
            subs(nums)
            print(resultado)

