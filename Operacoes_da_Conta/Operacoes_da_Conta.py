LIMITE_SAQUE = 3
numeros_de_saques = 0
saldo = 0
limite_de_Saque = 500
extrato = ""

menu = ("""
      \n
      ====================
      Escolha uma Operação
      ====================
      
      ------------
      [1] Depósito
      ------------
      [2] Saque
      ------------
      [3] Extrato
      ------------
      [0] Sair
      ------------
      \n
      """)
while True:
    print(menu)
    opcao = input("")
    
    if opcao == "1":
        valor_de_operacao = float(input("\nInforme o valor do depósito"))
        
        if valor_de_operacao > 0:
            saldo += valor_de_operacao
            extrato += f"Valor do Depósito R$: {valor_de_operacao:.2f}\n"
        else:
            print("Valor invalido, insira um número acima de 0")
            
            
    elif opcao == "2":
        valor_de_operacao = float(input("\nEfetue um saque. O limite de saque por vez é R$500: "))

        if numeros_de_saques >= LIMITE_SAQUE:
            print("\nNúmero de saques diários excedido.")
            
        elif valor_de_operacao > limite_de_Saque:
            print("\nValor de saque acima do permitido.\nTente novamente!")

        elif valor_de_operacao <= 0:
            print("\nValor inválido!\nTente novamente!")

        elif valor_de_operacao > saldo:
            print("\nSaldo insuficiente!\n")

        else:
            numeros_de_saques += 1
            saldo -= valor_de_operacao
            extrato += f"Saque: R$ {valor_de_operacao:.2f}\n"
            print("\nSaque realizado com sucesso.")
            
    elif opcao == "3":
        print("\n=================EXTRATO=================")
        print("Não foram realizadas movimentações" if not extrato else extrato) #if not verifica se a variável extrato continua vazia
        print(f"\nSaldo na conta R$: {saldo:.2f}\n")
        print("===========================================")
    
    elif opcao == "0":
        break
    
    else:
        print("Opção invalida, tente novamente")
    
