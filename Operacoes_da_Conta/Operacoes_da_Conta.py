# Refatorado com POO avançado usando @property e abc
from datetime import datetime as dt, timedelta as td
import textwrap
import json
import os
from abc import ABC, abstractmethod

# Caminhos dos arquivos
CAMINHO_USUARIOS = r"C:\\Users\\joaov\\Desktop\\Conta_Bancaria\\usuarios.json"
CAMINHO_TRANSACOES = r"C:\\Users\\joaov\\Desktop\\Conta_Bancaria\\transacoes.json"

# Constantes globais
LIMITE_SAQUE = 3
LIMITE_TRANSFERENCIA = 10
LIMITE_VALOR_SAQUE = 500
MASCARA_PTBR = "%d/%m/%Y às %H:%M"

# ----- CLASSE ABSTRATA PARA CONTA -----
class ContaBase(ABC):
    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def transferir(self, valor):
        pass

    @abstractmethod
    def ver_extrato(self):
        pass

# ----- CLASSE CONTA COM @PROPERTY E HERANÇA DE CONTAABSTRACT -----
class Conta(ContaBase):
    def __init__(self):
        self._saldo = 0
        self._extrato = []
        self._saques_diarios = 0
        self._transferencias_diarias = 0
        self._ultimo_dia = dt.now().date()

    # Usando @property para controle seguro do saldo
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo.")
        self._saldo = valor

    def resetar_limites(self):
        if dt.now().date() != self._ultimo_dia:
            self._saques_diarios = 0
            self._transferencias_diarias = 0
            self._ultimo_dia = dt.now().date()

    def registrar_transacao(self, tipo, valor):
        data = dt.now().strftime(MASCARA_PTBR)
        self._extrato.append(f"{tipo}: R$ {valor:.2f} em {data}")

        transacoes = []
        if os.path.exists(CAMINHO_TRANSACOES):
            with open(CAMINHO_TRANSACOES, "r") as arq:
                transacoes = json.load(arq)

        transacoes.append({"tipo": tipo, "valor": valor, "data": data})
        limite = dt.now() - td(days=7)
        transacoes = [t for t in transacoes if dt.strptime(t["data"], MASCARA_PTBR) >= limite]

        with open(CAMINHO_TRANSACOES, "w") as arq:
            json.dump(transacoes, arq, indent=4)

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.registrar_transacao("Depósito", valor)
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        self.resetar_limites()
        if self._saques_diarios >= LIMITE_SAQUE:
            print("Limite de saques diários atingido.")
        elif valor > LIMITE_VALOR_SAQUE:
            print("Valor acima do limite permitido.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor inválido.")
        else:
            self._saldo -= valor
            self._saques_diarios += 1
            self.registrar_transacao("Saque", valor)

    def transferir(self, valor):
        self.resetar_limites()
        if self._transferencias_diarias >= LIMITE_TRANSFERENCIA:
            print("Limite de transferências diárias atingido.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor inválido.")
        else:
            self._saldo -= valor
            self._transferencias_diarias += 1
            self.registrar_transacao("Transferência", valor)

    def ver_extrato(self):
        print("\n========== EXTRATO ==========\n")
        if not self._extrato:
            print("Nenhuma movimentação.")
        else:
            for linha in self._extrato:
                print(linha)
        print(f"\nSaldo atual: R$ {self._saldo:.2f}\n")
        print("=============================")

# ----- CLASSE USUARIO -----
class Usuario:
    def __init__(self, cpf, senha):
        self.cpf = cpf
        self.senha = senha
        self.conta = Conta()

    def verificar_senha(self, senha):
        return self.senha == senha

# ----- CLASSE BANCO -----
class Banco:
    def __init__(self):
        self.usuarios = self.carregar_usuarios()

    def carregar_usuarios(self):
        if os.path.exists(CAMINHO_USUARIOS):
            with open(CAMINHO_USUARIOS, "r") as arq:
                dados = json.load(arq)
                return {cpf: Usuario(cpf, dados[cpf]["senha"]) for cpf in dados}
        return {}

    def salvar_usuarios(self):
        dados = {cpf: {"senha": usuario.senha} for cpf, usuario in self.usuarios.items()}
        with open(CAMINHO_USUARIOS, "w") as arq:
            json.dump(dados, arq, indent=4)

    def formatar_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11:
            raise ValueError("O CPF deve conter 11 dígitos")
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    def criar_conta(self):
        cpf = input("Digite o CPF: ")
        senha = input("Digite a senha: ")
        cpf_formatado = self.formatar_cpf(cpf)

        if cpf_formatado in self.usuarios:
            print("CPF já cadastrado!")
            return

        self.usuarios[cpf_formatado] = Usuario(cpf_formatado, senha)
        self.salvar_usuarios()
        print("Conta criada com sucesso!")

    def fazer_login(self):
        cpf = input("Digite seu CPF: ")
        senha = input("Digite sua senha: ")
        cpf_formatado = self.formatar_cpf(cpf)

        usuario = self.usuarios.get(cpf_formatado)
        if usuario and usuario.verificar_senha(senha):
            print("Login realizado com sucesso!")
            return usuario
        else:
            print("CPF ou senha incorretos.")
            return None

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário encontrado.")
            return
        print("\n====== USUÁRIOS CADASTRADOS ======")
        for i, cpf in enumerate(self.usuarios, start=1):
            print(f"Usuário: {cpf} - Conta: {i} - Agência: 0001")

# ----- MENUS -----
def menu_inicial():
    print("""
    ===== SISTEMA BANCÁRIO =====
    [1] Login
    [2] Criar Conta
    [3] Listar Usuários
    [0] Sair
    """)
    return input("Escolha uma opção: ")

def menu_principal():
    menu = ("""
      ====================
      Escolha uma Operação
      ====================
      [1] Depósito
      [2] Saque
      [3] Transferência
      [4] Extrato
      [0] Sair
    """)
    return input(textwrap.dedent(menu))

# ----- LOOP PRINCIPAL -----
def main():
    banco = Banco()
    while True:
        opcao = menu_inicial()
        if opcao == "1":
            usuario = banco.fazer_login()
            if usuario:
                while True:
                    escolha = menu_principal()
                    if escolha == "1":
                        valor = float(input("Informe o valor para depósito: "))
                        usuario.conta.depositar(valor)
                    elif escolha == "2":
                        valor = float(input("Informe o valor para saque: "))
                        usuario.conta.sacar(valor)
                    elif escolha == "3":
                        valor = float(input("Informe o valor para transferência: "))
                        usuario.conta.transferir(valor)
                    elif escolha == "4":
                        usuario.conta.ver_extrato()
                    elif escolha == "0":
                        break
                    else:
                        print("Opção inválida.")
        elif opcao == "2":
            banco.criar_conta()
        elif opcao == "3":
            banco.listar_usuarios()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


main()