menu = '''


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


# função depositar

def depositar():
    print('        Deposito        ')
    print('-------------------------')
    valor_deposito = int(input('Deseja fazer um deposito em qual valor: '))
    if valor_deposito <= 0:
        print('Valor de saque precisa ser positivo e maior que zero!')
        return depositar()
    elif valor_deposito > 0:
        print(f'O seu deposito no valor de R${valor_deposito}, foi realizado com sucesso!')

# função sacar

def sacar():
    print('|      Saque        |')
    print('---------------------')
    valor_saque = int(input('Deseja realizar um saque em qual valor?  '))
    if valor_saque < saldo:
        print('Saldo insulficiente')
        return saldo, numero_saques
    if valor_saque <= saldo:
        print('O valor precisa ser maior que zero.')
        return saldo, numero_saques
    if valor_saque > 500:
        print('Valor de saque excedido! Se precisar peça ajuda para algum de nossos funcionários.')
        return saldo, numero_saques
    
    saldo -= valor_saque
    numero_saques += 1
    print(f'Saque no valor de R${valor_saque:.2f} realizado com sucesso.')
    return saldo, numero_saques

while True:

    opcao = input(menu)
    if opcao == 'd':
        depositar()
    elif opcao == 's':
        sacar()


        