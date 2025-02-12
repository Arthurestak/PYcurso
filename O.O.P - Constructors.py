# Cria Classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_de_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento
        
    def usuario_completo(self):
        print(self.nome,self.sobrenome,self.data_de_nascimento)

# Cria o Objeto
usuario = Funcionarios('Arthur', 'Oliveira', '14/02/2007')
usuario2 = Funcionarios('Pedro', 'Silva', '10/09/2006')

# Print
usuario.usuario_completo()

