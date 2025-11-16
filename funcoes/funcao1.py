import this
import codecs

# função é um bloco de código identificado por um nome e pode receber
# uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões. Usar funções torna o 
# código mais legível e possibilita o reaproveitamento de código. 
# Programar baseado em funções, é o mesmo que dizer que estamos programando 
# de forma estruturada

# def - palavra reservada para identificar a função
def saudacao():
    print("Olá Mundo")

saudacao()

def mensagem(nome):
    print(f'o meu nome é {nome}')

mensagem(nome='Sérgio')

# argumentos nomeados
# passa o valor para uma função
# usando o nome do parâmetro

def carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

carro('fiat', 'palio','1998', 'NFE-3639')

# Args e kwargs

# *Args vem como uma tupla
# **Kwargs vem como um dicionário

zen_code = this.s
zen = codecs.decode(zen_code,'rot13')

def poema(data,*args, **kwargs):
    texto = '\n'.join(args)
    dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])

    mensagem =f'{data}\n\n{texto}\n\n{dados}'
    print(mensagem)

poema(zen)