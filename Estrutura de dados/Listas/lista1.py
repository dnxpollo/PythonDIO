# listas

# lista em Python é uma sequencia de itens objeto.

frutas = ['laranja', 'maca', 'uva']

legumes = []

letras = list('python')
numeros = list(range(10))

carro = ['ferrari', 'f8', 4200000, 2020, 2900, 'São Paulo', True]

# para acessar algum dos elementos da lista, podemos usar o indice.
# começa do zero, mas para começar do final da lista podemos usar o -1.

# a lista é um objeto, e podemos usar listas aninhadas.

matriz = [
    [1, 'a', 2]
    ['b', 3, 4]
    [5, 6, 'c']
]

# Fatiamento
# Podemos extrair um conjunto de valores da sequência
# voltar a branch modulo-1 para ver mais sobre fatiamento de strings

# iterar listas
# forma mais comum para percorrer os dados de uma lista é utilizando o comando for.

# função enumerate
# quando necessário saber qual o índice do objeto dentro do laço for.

carros = ['gol', 'celta', 'palio']

for indice, carro in enumerate(carros):
    print(f'{indice: {carro}}')

# Compreensão de listas
# oferece sintaxe reduzida quando:
# criar lista com base nos valores de uma lista já existente(filtro)
# ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente

numeros = [1, 2, 3, 4, 5, 6, 7]
pares = []

# list for
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# list compreention
numeros = [1, 2, 3, 4, 5, 6, 7]
pares = [numero for numero in numeros if numero % 2 == 0]

