# 💰 Sistema Bancário em Python (Versão com Autenticação e JSON)

## 📌 Objetivo Geral

Desenvolver um **sistema bancário via terminal**, com múltiplos usuários e autenticação via **CPF e senha**, utilizando arquivos `.json` para persistência dos dados.

Este projeto visa reforçar a lógica de programação, manipulação de arquivos, controle de fluxo e estrutura de dados com dicionários em Python.

---

## ⚙️ Funcionalidades

### ✅ Login e Cadastro de Usuário
- Login realizado com **CPF e senha**.
- Cadastro com verificação de duplicidade de CPF.
- Armazenamento seguro dos usuários no arquivo `usuarios.json`.

### ✅ Depósito
- Permite depósitos com valores maiores que 0.
- Atualiza saldo e registra no extrato.
- Transações são salvas em `transacoes.json`.

### ✅ Saque
- Limite de **3 saques por dia**, reiniciado automaticamente a cada novo dia.
- Limite de **R$ 500,00 por saque**.
- Verifica saldo disponível antes de sacar.
- Registra cada saque no extrato.

### ✅ Transferência
- Permite até **10 transferências por dia** por usuário.
- Bloqueia valores inválidos ou superiores ao saldo.
- Registra data, hora e valor da transação no extrato.

### ✅ Extrato
- Mostra o histórico completo de **depósitos**, **saques** e **transferências**.
- Exibe o **saldo atual** da conta.
- Caso não haja movimentações, informa ausência de extrato.

### ✅ Listagem de Usuários
- Lista todos os usuários cadastrados com formato:
    Usuário: CPF - Conta: X - Agência: 0001
---

## 🛠️ Recursos Técnicos Utilizados

- `input()` para entrada de dados via terminal  
- `print()` com `f-strings` para formatação  
- `json` para leitura/escrita de arquivos  
- `os.path.exists()` para verificação de arquivos  
- `datetime` para controle de data e hora  
- `textwrap.dedent` para organizar o menu visualmente  
- Funções e modularização do código  
- Validação de CPF e formatação padrão (`XXX.XXX.XXX-XX`)

---

## 🧠 Conceitos Praticados

- Estrutura de repetição `while`  
- Condicionais `if`, `elif`, `else`  
- Manipulação de arquivos JSON  
- Controle de fluxo baseado em data (limites diários)  
- Lógica de autenticação básica  
- Funções com escopo global/local  
- Simulação de regras bancárias reais  

---

## 🗃️ Estrutura de Arquivos

Conta_Bancaria/ │ ├── usuarios.json # Armazena usuários cadastrados (CPF + senha) ├── transacoes.json # Armazena histórico de transações por tipo └── Operacoes_da_Conta/ └── operacoes_da_conta.py # Arquivo principal com a lógica do sistema

yaml
Copiar código

---

## 🚀 Próximos Passos (Sugestões de Evolução)

- Associar número de conta único por usuário (fixo)  
- Separar cada usuário com suas próprias transações  
- Utilizar **Programação Orientada a Objetos (POO)**  
- Implementar interface gráfica com `Tkinter` ou versão web com `Flask`  
- Armazenar dados em banco de dados como SQLite ou PostgreSQL  
- Criptografar senhas com `hashlib` ou `bcrypt`  

---

### 👨‍💻 Desenvolvido por:  
**João Vitor de Lima Sampaio**  
[LinkedIn](http://www.linkedin.com/in/jo%C3%A3o-vitor-de-lima-sampaio-1566a124a) | [GitHub](https://github.com/Joaovitorsamps?tab=repositories)