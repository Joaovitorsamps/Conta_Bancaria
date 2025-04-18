import datetime as dt

LIMITE_SAQUE = 3
LIMITE_TRANSFERENCIA = 10
numeros_de_transferencia = 0
numeros_de_saques = 0
saldo = 0
limite_de_Saque = 500
extrato = ""
MASCARA_PTBR = "%d/%m/%Y às %H:%M"
ultimo_dia = dt.datetime.now().date()  # Salva o dia atual

menu = ("""
      \n
      ====================
      Escolha uma Operação
      ====================
      
      -----------------
      [1] Depósito
      -----------------
      [2] Saque
      -----------------
      [3] Transferência
      -----------------
      [4] Extrato
      -----------------
      [0] Sair
      -----------------
      \n
      """)

while True:
    # Atualiza data e verifica se virou o dia
    data_atual = dt.datetime.now()
    hoje = data_atual.date()

    if hoje != ultimo_dia:
        numeros_de_saques = 0
        numeros_de_transferencia = 0
        ultimo_dia = hoje
        print("\nNovo dia iniciado. Limites de saque e transferência foram resetados.\n")

    print(menu)
    opcao = input("")

    if opcao == "1":
        valor_de_operacao = float(input("\nInforme o valor do depósito\n"))

        if valor_de_operacao > 0:
            saldo += valor_de_operacao
            extrato += f"Valor do Depósito R$: {valor_de_operacao:.2f} no dia {data_atual.strftime(MASCARA_PTBR)}\n"
        else:
            print("Valor inválido, insira um número acima de 0")

    elif opcao == "2":
        valor_de_operacao = float(input("\nEfetue um saque. O limite de saque por vez é R$500: \n"))

        if numeros_de_saques >= LIMITE_SAQUE:
            print("\nNúmero de saques diários excedido.")
        elif valor_de_operacao > limite_de_Saque:
            print("\nValor de saque acima do permitido.")
        elif valor_de_operacao <= 0:
            print("\nValor inválido.")
        elif valor_de_operacao > saldo:
            print("\nSaldo insuficiente!")
        else:
            numeros_de_saques += 1
            saldo -= valor_de_operacao
            extrato += f"Saque: R$ {valor_de_operacao:.2f} no dia {data_atual.strftime(MASCARA_PTBR)}\n"
            print("\nSaque realizado com sucesso.")

    elif opcao == "3":
        valor_de_operacao = float(input("\nInforme o valor desejado para transferência\n"))

        if numeros_de_transferencia >= LIMITE_TRANSFERENCIA:
            print("\nVocê chegou ao limite de transferências, tente novamente amanhã")
        elif valor_de_operacao <= 0:
            print("\nValor inválido.")
        elif valor_de_operacao > saldo:
            print("\nSaldo insuficiente!")
        else:
            numeros_de_transferencia += 1
            saldo -= valor_de_operacao
            extrato += f"Transferência realizada no valor de: R$ {valor_de_operacao:.2f} no dia {data_atual.strftime(MASCARA_PTBR)}\n"
            print("\nTransferência realizada com sucesso.\n")

    elif opcao == "4":
        print("\n=================EXTRATO=================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo na conta R$: {saldo:.2f}\n")
        print("===========================================")

    elif opcao == "0":
        break

    else:
        print("Opção inválida, tente novamente.")
