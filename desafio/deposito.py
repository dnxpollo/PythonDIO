menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

# Variáveis principais
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

# Função depositar
def depositar(saldo, extrato):
    print('        Depósito        ')
    print('-------------------------')
    valor_deposito = int(input('Deseja fazer um depósito em qual valor: '))

    if valor_deposito <= 0:
        print('Valor precisa ser positivo e maior que zero!')
        return saldo, extrato  # ❗ Corrigido: não chama a função de novo

    saldo += valor_deposito
    extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
    print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!')
    return saldo, extrato

# Função sacar
def sacar(saldo, extrato, numero_saques):
    print('|      Saque        |')
    print('---------------------')
    valor_saque = int(input('Deseja realizar um saque em qual valor?  '))

    if valor_saque <= 0:
        print('O valor precisa ser maior que zero.')
        return saldo, extrato, numero_saques

    if valor_saque > limite:
        print('Valor de saque excedido! Limite é R$500.00.')
        return saldo, extrato, numero_saques

    if valor_saque > saldo:
        print('Saldo insuficiente.')
        return saldo, extrato, numero_saques

    if numero_saques >= LIMITE_SAQUES:
        print('Limite diário de saques atingido.')
        return saldo, extrato, numero_saques

    saldo -= valor_saque
    extrato += f'Saque: R$ {valor_saque:.2f}\n'
    numero_saques += 1
    print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso.')
    return saldo, extrato, numero_saques

# Função extrato
def exibir_extrato(saldo, extrato):
    print('\n========== EXTRATO ==========')
    print(extrato if extrato else 'Nenhuma movimentação realizada.')
    print(f'Saldo atual: R$ {saldo:.2f}')
    print('==============================\n')

# Loop principal
while True:
    opcao = input(menu)

    if opcao == 'd':
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == 's':
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)

    elif opcao == 'e':
        exibir_extrato(saldo, extrato)

    elif opcao == 'q':
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida. Tente novamente.')


