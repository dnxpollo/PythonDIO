# Objetos de primeira classe

def somar(a, b):
    return a + b

def substrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, substrair)

# Escopo local e Global
# Local - dentro do bloco da função
# Global -  Não deve ser utilizado



def salario_bonus(bonus):
    salario = 2000
    salario += bonus
    return salario


print(salario_bonus(500))

