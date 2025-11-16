# while
# Usado para repetir um bloco de código várias vezes.
# Lógica: Usar quando não se sabe 
# quantas vezes executar um código

opcao = -1

while opcao != 0:
    opcao = int(input("Opção:  \n[1] Sacar \n[2] Extrato \n[0] Sair \n Informe uma opção: "))

    if opcao == 1:
        print("Sacando o dinheiro, retire na boca do caixa!")
    elif opcao == 2:
        print("Imprimindo extrato!")
    elif opcao == 0:
        print("Obrigado por confiar em nossos serviços!")
    else:
        print("Informe uma opção válida!")


# break 
# utilizado para encerrar a execução do código

opcao = -1

while opcao != 0:
    opcao = int(input("Informe um número: "))
    if opcao == 10:
        break
    elif opcao % 2 == 0:
        print("preso no loop")
    else:
        break

# continue
# usado para escapar uma exceção

for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=' ')

