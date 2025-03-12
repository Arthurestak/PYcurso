'''
LER:

arquivo = open('textoTeste.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

with open('textoTeste.txt','r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
'''

'''
ESCREVER: 

arquivo = open('textoTeste.txt','w')
arquivo.write('ALOU!')
arquivo.close()

OU

with open('textoTeste.txt','w') as arquivo:
    arquivo.write('Hellow!')
    arquivo.close()
'''


