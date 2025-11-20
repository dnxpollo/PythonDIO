from datetime import datetime

menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
transacoes = []

def depositar(saldo, transacoes):
    if len(transacoes) >= LIMITE_TRANSACOES:
        print("Limite diário de transações atingido!")
        return saldo, transacoes

    valor_deposito = int(input('Deseja fazer um depósito em qual valor: '))
    if valor_deposito <= 0:
        print('Valor precisa ser positivo e maior que zero!')
        return saldo, transacoes

    saldo += valor_deposito
    hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    transacoes.append({"tipo": "Depósito", "valor": valor_deposito, "hora": hora})
    print(f"{hora} - Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
    return saldo, transacoes

def sacar(saldo, transacoes, numero_saques):
    if len(transacoes) >= LIMITE_TRANSACOES:
        print("Limite diário de transações atingido!")
        return saldo, transacoes, numero_saques

    valor_saque = int(input('Deseja realizar um saque em qual valor?  '))
    if valor_saque <= 0:
        print('O valor precisa ser maior que zero.')
        return saldo, transacoes, numero_saques
    if valor_saque > limite:
        print('Valor de saque excedido! Limite é R$500.00.')
        return saldo, transacoes, numero_saques
    if valor_saque > saldo:
        print('Saldo insuficiente.')
        return saldo, transacoes, numero_saques
    if numero_saques >= LIMITE_SAQUES:
        print('Limite diário de saques atingido.')
        return saldo, transacoes, numero_saques

    saldo -= valor_saque
    numero_saques += 1
    hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    transacoes.append({"tipo": "Saque", "valor": valor_saque, "hora": hora})
    print(f"{hora} - Saque de R$ {valor_saque:.2f} realizado com sucesso.")
    return saldo, transacoes, numero_saques

def exibir_extrato(saldo, transacoes):
    print('\n========== EXTRATO ==========')
    if not transacoes:
        print('Nenhuma movimentação realizada.')
    else:
        for t in transacoes:
            print(f"{t['hora']} - {t['tipo']}: R$ {t['valor']:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print('===============================\n')

while True:
    opcao = input(menu)

    if opcao == 'd':
        saldo, transacoes = depositar(saldo, transacoes)
    elif opcao == 's':
        saldo, transacoes, numero_saques = sacar(saldo, transacoes, numero_saques)
    elif opcao == 'e':
        exibir_extrato(saldo, transacoes)
    elif opcao == 'q':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
