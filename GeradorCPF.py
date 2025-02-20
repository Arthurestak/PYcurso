import os 
import random as rd

while True:
    decrescenteUm = 10

    contador = 9

    cpf_nove_digitos = []

    while contador >= 1:
        cpf_nove_digitos.append(rd.choice(range(0,10)))
        contador -= 1  
        continue
    os.system('cls')
    
    if len(cpf_nove_digitos) == 9:

        cpf_multi = []

        for i in cpf_nove_digitos:

            try:
                iNum = int(i)
            except:
                os.system('cls')
                print('Digite um valor válido!')
                continue

            multi = decrescenteUm * iNum

            cpf_multi.append(multi)

            decrescenteUm -= 1

        a,b,c,d,e,f,g,h,i = cpf_multi

        soma = a+b+c+d+e+f+g+h+i    

        multi2 = soma * 10

        resto = multi2 % 11

        if resto >= 10:
            print('O próximo número do CPF é: 0')
        break
    else:
        print('Digite um valor válido, apenas os 9 primeiros números!\n')
        continue

decrescenteDois = 11


cpf_novo_lista = []
for i in cpf_nove_digitos:
    cpf_novo_lista.append(i)
cpf_novo_lista.append(resto) if resto <= 9 else cpf_novo_lista.append(0)
    
cpf_multi2 = []
cpf_completo = []
for i in cpf_novo_lista:
    iNum = int(i)
    multi3 = decrescenteDois * iNum
    cpf_multi2.append(multi3)
    decrescenteDois -= 1 
j,k,l,m,n,o,p,q,r,s = cpf_multi2
soma2 = j+k+l+m+n+o+p+q+r+s
multi4 = soma2 * 10    
resto2 = multi4 % 11
if resto2 <= 9:
    cpf_novo_lista.append(resto2)
    print('CPF gerado: ',"".join(map(str,cpf_novo_lista)))
else:
    cpf_novo_lista.append(0)
    print('CPF gerado: ',"".join(map(str,cpf_novo_lista)))

