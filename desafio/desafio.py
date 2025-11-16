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

while True:

    opcao = input(menu)


    if opcao == 'd':
        deposito = int(input('Deseja fazer um deposito em qual valor: '))
        print('Deposito')
        ('--------------')
        print(f'O seu deposito foi feito no valor de R${deposito}. Deseja voltar ao menu ? [1] Sim [2] Encerrar programa')
        deposito =+ saldo
        opcao_deposito = int(input('Qual opção devemos seguir? '))
        if opcao_deposito == 1:
            continue
        else:
            break
    elif opcao == 's':
        print('Saque')
        print("---------")
        valor_saque = int(input('Deseja realizar um saque em qual valor?  '))
        if valor_saque < saldo:
            print('Saldo insulficiente. Caso necessário, entre em contato com seu gerente.')
            continue
        elif valor_saque <= 0:
            print('O valor precisa ser maior que zero.')
            continue
        elif valor_saque > 500:
            print('O valor limite para saques é R$500.0!')
        elif valor_saque > saldo:
            numero_saques = +1
            saldo = valor_saque - saldo 

    elif opcao == 'e':
        print('Extrato')
    elif opcao == 'q':
        print('Sair')
        break
    else:
        print('Opção inválida. Escolha uma opção do menu')

