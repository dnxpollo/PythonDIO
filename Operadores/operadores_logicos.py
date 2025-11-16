# operador_comparacao + operador_logico + operador_comparacao...

saldo = 1000
saque = 200
limite = 100
conta_especial = True

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

# and | or | not
#parantenses ajudam a delimitar quem terá a precedência

print('------------------------')
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)


exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_especial_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)