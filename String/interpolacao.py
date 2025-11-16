espaco = "------------------------------------------"

#old style %

nome = 'sérgio'
idade = 28
profissao = 'programador'
linguagem = 'python'

print('olá, me chamo %s. tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' %(nome, idade, profissao, linguagem)) # maneira antigamente usada para interpolação, criada no Python 2.

# Método format
print(espaco)

nome = 'sérgio'
idade = 28
profissao = 'programador'
linguagem = 'python'

print('olá, me chamo {}. tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))

print('olá, me chamo {3}. tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {0}.'.format(linguagem, idade, profissao, nome))

# f-string
print(espaco)

nome = 'sérgio'
idade = 28
profissao = 'programador'
linguagem = 'python'

print(f'olá, me chamo {nome}. tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}')

# definir numero de casas após a virgula

saldo = 43.896
print(f'{saldo} e {saldo:.2f}')
