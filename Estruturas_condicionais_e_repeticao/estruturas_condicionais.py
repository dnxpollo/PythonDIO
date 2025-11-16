# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

# if | elif | else
# Usamos para criar uma estrutura condicional simples, composta por um único desvio
# O comando testa a expressão lógica, e em caso de verdadeiro as instruções do bloco serão executadas

saldo = 2000.0
saque = float(input("Informe o valor a ser sacado: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

opcao = int(input("Opção:  \n[1] Sacar \n[2] Extrato \n Informe uma opção: "))

if opcao == 1:
    print("Sacando o dinheiro, retire na boca do caixa!")
elif opcao == 2:
    print("Imprimindo extrato!")
else:
    print("Informe uma opção válida!")

# Estruturas condicionais aninhadas

conta_normal = True
conta_universitaria: False
conta_especial = True

saldo = 2000
saque = 2600
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque < (saldo + cheque_especial):
        print("Saque realizado com cheque especial")
    else:
        print("Não foi possivel realizar o saque. Saque insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= saque:
        print("Saque realizado com cheque especial")
    else:
        print("Não foi possivel realizar o saque. Saque insuficiente!")
elif conta_especial:
    print("Conta especial selecionada!")
else:
    print("Tipo de conta não consta no sistema!")



# if ternario
# Permite escrever uma condição em uma única linha. 
# É composto por três partes, a primeira parte é o 
# retorno caso a expresão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

saldo = 200
saque = 250

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque")