# Indentação em Python funciona tanto para manter um código organizado e legivel quanto para 
# e terminar onde um bloco de comando começa e onde ele termina

# Enquanto outras linguagens de programaçao usam chaves {} para delimitar um bloco de código, o Python usa a indentação/tabulações para definir o bloco de código.

# Caso a indentação/tabulação não esteja conforme a engine entende, a própria engine
# vai devolver um erro, que pode ser IndentationError ou SyntaxError.

def saudacao():
    print("Olá, Sérgio")  #indentação correta

# Esse código vai gerar um erro.
#def saudacao():
#print("Olá, Sérgio")
 

# Usar 4 espaços por nível de indentação(padrão recomendado pelo PEP 8)
# Evitar intercalar espaços e tab 

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado")
        print("retire o seu dinheiro na boca do caixa.")
    elif saldo < valor:
        print("Saldo insulficiente")
        print("Obrigado por ser nosso cliente, tenha um bom dia!")
sacar(2000)