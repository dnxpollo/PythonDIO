from datetime import datetime

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
transacoes = []
usuarios = []
conta_corrente = []
mascara_data_nascimento = '%d/%m/%Y'

# Função Menu
def menu():
    return '''
    [c] Cadastrar cliente
    [a] Cadastrar Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [lc] Listar contas
    [q] Sair
    '''

# Função Depositar
def depositar(saldo, transacoes, /):
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

# Função Sacar
def sacar(*, saldo, transacoes, numero_saques, limite):
    if len(transacoes) >= LIMITE_TRANSACOES:
        print("Limite diário de transações atingido!")
        return saldo, transacoes, numero_saques

    valor_saque = int(input('Deseja realizar um saque em qual valor? '))
    if valor_saque <= 0:
        print('O valor precisa ser maior que zero.')
        return saldo, transacoes, numero_saques
    if valor_saque > limite:
        print(f'Valor de saque excedido! Limite é R${limite:.2f}.')
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
    print(f'Você realizou {numero_saques} saque(s). O limite diário é {LIMITE_SAQUES}!')
    return saldo, transacoes, numero_saques

# Função Exibir Extrato
def exibir_extrato(saldo, /, *, transacoes=transacoes):
    print('\n========== EXTRATO ==========')
    if not transacoes:
        print('Nenhuma movimentação realizada.')
    else:
        for t in transacoes:
            print(f"{t['hora']} - {t['tipo']}: R$ {t['valor']:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print('===============================\n')

# Função Cadastrar Usuário
def cadastrar_usuario():
    cpf = input('Informe seu CPF: ')
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print('CPF já cadastrado.')
            return usuarios
        
    nome = input('Informe seu nome completo: ')
    data_nascimento_input = input(f'{nome}, insira sua data de nascimento (dd/mm/aaaa): ')
    try:
        data_nascimento = datetime.strptime(data_nascimento_input, mascara_data_nascimento)
    except ValueError:
        print("Data inválida! Use o formato dd/mm/aaaa.")
        return usuarios

    logradouro = input('Informe o logradouro: ')
    numero_endereco = int(input('Informe o número: '))
    bairro = input('Informe o bairro: ')
    cidade_endereco = input('Informe a cidade: ')
    estado = input('Informe a sigla do seu Estado: ')

    endereco = {
        'logradouro': logradouro,
        'número_endereco': numero_endereco,
        'bairro': bairro,
        'cidade_endereco': cidade_endereco,
        'estado': estado
    }

    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    usuarios.append(novo_usuario)
    print('Usuário cadastrado com sucesso!')

# Função cadastrar_conta
def cadastrar_conta(usuarios, conta_corrente, cpf):
    numero_agencia = '0001'
    numero_conta = len(conta_corrente) + 1
    
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print('Usuário não encontrado. Cadastre um usuário!')
        return conta_corrente

    nova_conta_corrente = {
        'numero_agencia': numero_agencia,
        'numero_conta': numero_conta,
        'usuario': usuario
    }

    conta_corrente.append(nova_conta_corrente)
    print('Conta cadastrada com sucesso!')
    return conta_corrente

# Função listar contas
def listar_contas(conta_corrente):
    print("\n=== CONTAS CADASTRADAS ===")
    if not conta_corrente:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in conta_corrente:
            print(f"Agência: {conta['numero_agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
    print("===========================\n")

# Loop principal
while True:
    opcao = input(menu())

    if opcao == 'd':
        saldo, transacoes = depositar(saldo, transacoes)
    elif opcao == 's':
        saldo, transacoes, numero_saques = sacar(saldo=saldo, transacoes=transacoes, numero_saques=numero_saques, limite=limite)
    elif opcao == 'e':
        exibir_extrato(saldo, transacoes=transacoes)
    elif opcao == 'c':
        cadastrar_usuario()
    elif opcao == 'a':
        cpf = input('Informe o CPF do titular da conta: ')
        cadastrar_conta(usuarios, conta_corrente, cpf)
    elif opcao == 'lc':
        listar_contas(conta_corrente)
    elif opcao == 'q':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
