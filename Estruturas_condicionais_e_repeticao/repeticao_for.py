# for e while
# São estruturas usadas para repetir um trecho de código um (in)determinado número de vezes. 

texto = input("Informe um texto: ")
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')

print()
print('Executar')


