# métodos de fabrica são métodos que retornam uma nova instância
# métodos estáticos são usados para criar funções


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade > 18
    
p = Pessoa.criar_data_nascimento(28, 6, 28, 'Sérgio')
print(p.nome, p.idade)

print(Pessoa.maior_idade(28))
print(Pessoa.maior_idade(8))