pessoa = {}

pessoa['nome'] = 'Arthur'

pessoa['sobrenome'] = 'Oliveira'

if (pessoa.get('sobrenome')):
    print(f'{pessoa['sobrenome']} existe!')
else:
    print('Erro!')