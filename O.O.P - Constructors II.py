from datetime import datetime

class Funcionarios():
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        print(self.nome, self.sobrenome, self.ano_nascimento)

    def idade_funcionario(self):
        ano_numero = int(self.ano_nascimento)
        ano_atual = datetime.now().year
        idade = ano_atual - ano_numero
        print(f'O funcionário tem {idade} anos de idade!')
        
usuario1 = Funcionarios('Arthur', 'Oliveira', '2007')

Funcionarios.idade_funcionario(usuario1)