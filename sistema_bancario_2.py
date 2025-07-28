menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        if valor >0:
            saldo += valor
            extrato += f"Deposito no valor de R$ {valor:.2f}\n"
        else:
            print("Operação invalida! Reinicie a Operação e insira um valor valido.") 

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insulficiente. Tente outro valor!")
        
        elif excedeu_limite:
            print("Valor superior ao limite diário. Tente outro valor!")
        elif excedeu_saques:
            print("O numero de saques por dia foi excedido. Operação não realizada")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque no valor de R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação não realizada! O valor informado é inválido!")

    elif opcao == "e":
        print("\n ================EXTRATO===================")
        print("Não houveram movimentações no período." if not extrato else extrato)
        print(f"\n Saldo R$ {saldo:.2f}")
        print("==============================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Selecione umas das opções apresentadas no menu.")



