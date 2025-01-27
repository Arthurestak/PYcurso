numero_1=input('Digite um número:')
numero_2=input('Digite outro número:')
try:
    numero_int_1=int(numero_1)
    numero_int_2=int(numero_2)

    soma= numero_int_1+numero_int_2
    print(f'A soma dos dois números é: {soma}')
except ValueError:
    print(f'Você não digitou números!')