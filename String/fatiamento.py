# Fatiamento de string é uma técnica utilizada para retornar substrings (partes da string original), # 
# informando inicio (start), fim(stop) e passo(step):[start: stop[, step]]

nome = 'Sérgio Henrique Ferreira de Andrade'

print(nome[0]) # primeira letra na variavel nome

print(nome[:6]) # não defini o start(começa do zero por padrão), e para no indice 5]

print(nome[7:]) # define o inicio

print(nome[6:10:2]) #inicio:fim:step

print(nome[:]) # inclui a string inteira

print(nome[::-1]) # inclui a string de trás para frente