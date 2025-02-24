# lista = [10,8,5,7,8,9,1]

# lista_nova = []

# contador = 0

# while len(lista_nova) < len(lista) :  
#     contador += 1 
#     if contador in lista:
#         lista_nova.append(contador)
#         print(lista_nova) 
#     continue

import pandas as pd

# autoId = 1   

alunos = {
    'Nome' : ['Arthur','Gabriel','Pedro','Luis'],
    'Situação' : ['Aprovado','Reprovado','Reprovado','Aprovado'],
    'ID' : [1,2,3,4]
}
                                      
alunosDF = pd.DataFrame(alunos)

print(alunosDF.loc[alunosDF['Situação'] == 'Reprovado'])