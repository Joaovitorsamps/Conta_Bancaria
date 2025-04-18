from datetime import datetime as dt, timedelta as td
import textwrap
import json
import os

# Caminhos dos arquivos
CAMINHO_USUARIOS = r"C:\Users\joaov\Desktop\Conta_Bancaria\usuarios.json"
CAMINHO_TRANSACOES = r"C:\Users\joaov\Desktop\Conta_Bancaria\transacoes.json"

# Constantes de limite
LIMITE_SAQUE = 3
LIMITE_TRANSFERENCIA = 10
limite_de_Saque = 500
MASCARA_PTBR = "%d/%m/%Y às %H:%M"

# Variáveis de controle
data_atual = dt.now()
ultimo_dia = data_atual.date()
saldo = 0
numeros_de_saques = 0
numeros_de_transferencia = 0
extrato = ""

# ----- Funções utilitárias -----
def formatar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        raise ValueError("O CPF deve conter 11 dígitos")
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# ----- Função para menu inicial -----
def menu_inicial():
    print("""
    ===== SISTEMA BANCÁRIO =====
    [1] Login
    [2] Criar Conta
    [3] Listar Usuários
    [0] Sair
    """)
    return input("Escolha uma opção: ")

# ----- Função para o menu principal -----
def menu():
    menu = ("""
      \n
      ====================
      Escolha uma Operação
      ====================
      
      ----------------------  |  
      [1] Depósito            |  
      ----------------------  |  
      [2] Saque               |  
      ----------------------  |
      [3] Transferência       |
      ----------------------  |
      [4] Extrato             |
      ----------------------  |
      [0] Sair                |
      ----------------------  |
      \n
      """)
    return input(textwrap.dedent(menu))

# ----- Função de login -----
def fazer_login():
    cpf = input("\nDigite seu CPF: ")
    senha = input("Digite sua senha: ")
    cpf_formatado = formatar_cpf(cpf)

    try:
        with open(CAMINHO_USUARIOS, "r") as arq:
            usuarios = json.load(arq)
        if cpf_formatado in usuarios and usuarios[cpf_formatado]["senha"] == senha:
            print("Login realizado com sucesso!")
            return True
        else:
            print("CPF ou senha incorretos.")
            return False
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
        return False

# ----- Função para criar nova conta -----
def criar_conta():
    cpf = input("Digite o CPF: ")
    senha = input("Digite a senha: ")
    cpf_formatado = formatar_cpf(cpf)

    usuarios = {}
    if os.path.exists(CAMINHO_USUARIOS):
        with open(CAMINHO_USUARIOS, "r") as arq:
            usuarios = json.load(arq)

    if cpf_formatado in usuarios:
        print("CPF já cadastrado!")
        return

    usuarios[cpf_formatado] = {"senha": senha}
    with open(CAMINHO_USUARIOS, "w") as arq:
        json.dump(usuarios, arq, indent=4)
    print("Conta criada com sucesso!")

# ----- Função para listar usuários existentes -----
def listar_usuarios():
    if not os.path.exists(CAMINHO_USUARIOS):
        print("Nenhum usuário encontrado.")
        return

    with open(CAMINHO_USUARIOS, "r") as arq:
        try:
            usuarios = json.load(arq)
            if not usuarios:
                print("Nenhum usuário encontrado.")
                return
            print("\n====== USUÁRIOS CADASTRADOS ======")
            for cpf in usuarios:
                print(f"Usuário: {cpf} - Conta: 1 - Agência: 0001")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de usuários.")

# ----- Função para registrar transações -----
def registrar_transacao(tipo, valor):
    data = dt.now().strftime(MASCARA_PTBR)
    nova = {"tipo": tipo, "valor": valor, "data": data}

    transacoes = []
    if os.path.exists(CAMINHO_TRANSACOES):
        with open(CAMINHO_TRANSACOES, "r") as arq:
            transacoes = json.load(arq)

    transacoes.append(nova)
    limite = dt.now() - td(days=7)
    transacoes = [t for t in transacoes if dt.strptime(t["data"], MASCARA_PTBR) >= limite]

    with open(CAMINHO_TRANSACOES, "w") as arq:
        json.dump(transacoes, arq, indent=4)

# ----- Operações principais -----
def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} em {dt.now().strftime(MASCARA_PTBR)}\n"
        registrar_transacao("Depósito", valor)
    else:
        print("Valor inválido para depósito.")

def sacar(valor):
    global saldo, numeros_de_saques, extrato
    if numeros_de_saques >= LIMITE_SAQUE:
        print("Limite de saques diários atingido.")
    elif valor > limite_de_Saque:
        print("Valor acima do limite permitido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor <= 0:
        print("Valor inválido.")
    else:
        saldo -= valor
        numeros_de_saques += 1
        extrato += f"Saque: R$ {valor:.2f} em {dt.now().strftime(MASCARA_PTBR)}\n"
        registrar_transacao("Saque", valor)

def transferir(valor):
    global saldo, numeros_de_transferencia, extrato
    if numeros_de_transferencia >= LIMITE_TRANSFERENCIA:
        print("Limite de transferências diárias atingido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor <= 0:
        print("Valor inválido.")
    else:
        saldo -= valor
        numeros_de_transferencia += 1
        extrato += f"Transferência: R$ {valor:.2f} em {dt.now().strftime(MASCARA_PTBR)}\n"
        registrar_transacao("Transferência", valor)

def ver_extrato():
    print("\n========== EXTRATO ==========\n")
    print("Nenhuma movimentação." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}\n")
    print("=============================")

# ----- Loop principal -----
def main():
    global numeros_de_saques, numeros_de_transferencia
    ultimo_dia = dt.now().date()

    while True:
        if dt.now().date() != ultimo_dia:
            numeros_de_saques = 0
            numeros_de_transferencia = 0

        opcao = menu_inicial()

        if opcao == "1":
            if fazer_login():
                while True:
                    escolha = menu()
                    if escolha == "1":
                        valor = float(input("Informe o valor para depósito: "))
                        depositar(valor)
                    elif escolha == "2":
                        valor = float(input("Informe o valor para saque: "))
                        sacar(valor)
                    elif escolha == "3":
                        valor = float(input("Informe o valor para transferência: "))
                        transferir(valor)
                    elif escolha == "4":
                        ver_extrato()
                    elif escolha == "0":
                        break
                    else:
                        print("Opção inválida.")
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

main()
