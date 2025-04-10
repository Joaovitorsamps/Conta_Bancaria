# 💰 Desafio Inicial - Sistema Bancário em Python

## 📌 Objetivo Geral

Desenvolver um **sistema bancário simples**, via terminal, com as seguintes operações:

- **Depósito**
- **Saque**
- **Visualização de Extrato**

Esse projeto visa praticar lógica de programação, estrutura de repetição e controle de fluxo em Python.

---

## ⚙️ Funcionalidades

### ✅ Operação de Depósito
- Permite inserir qualquer valor maior que 0.
- Cada valor depositado é **armazenado** e exibido posteriormente na operação de **extrato**.

### ✅ Operação de Saque
- O sistema permite **3 saques diários**.
- Cada saque possui um limite de **R$ 500,00** por operação.
- Caso o valor exceda o saldo disponível, é exibida uma mensagem informando a **falta de saldo**.
- Todos os saques são **registrados e exibidos no extrato**.

### ✅ Operação de Extrato
- Exibe todos os depósitos e saques realizados.
- Mostra o **saldo atual** da conta no formato `R$ XXX.XX`.
- Caso nenhuma operação tenha sido feita, exibe uma mensagem de ausência de movimentações.

---

## 🧠 O que foi utilizado

- ✅ **Variáveis** (armazenamento de saldo, extrato e limites)
- ✅ **Laço de repetição** `while` (estrutura principal do menu)
- ✅ **Condicionais** `if`, `elif`, `else` (controle de fluxo)
- ✅ **Função** `input()` para entrada de dados
- ✅ **Formatação de strings** com `f-strings`
- ✅ **Operadores aritméticos e lógicos**
- ✅ **Exibição de mensagens condicionais** com ternário (`if not extrato`)

---

## 📈 Curva de Aprendizado

Este desafio permitiu a aplicação prática de:

- 🧩 **Lógica condicional com múltiplos cenários** (valores inválidos, limite de saque, saldo insuficiente)
- 🔄 **Estrutura de repetição com controle de saída**
- 🧠 **Simulação de regras reais de um sistema bancário** (quantidade de saques, valores máximos, extrato formatado)
- 🛠️ **Tratamento de entradas e validações simples** (valores negativos, tipos numéricos)
- 💡 **Organização e clareza do código** para facilitar futuras expansões

---

## 🗃️ Código-fonte

Todo o código está contido no arquivo principal `sistema_bancario.py`. O sistema é executado inteiramente no terminal.

---

## 🚀 Próximos Passos (Sugestões de Evolução)

- Implementar autenticação de usuário
- Armazenar dados em arquivos ou banco de dados
- Criar um sistema de contas múltiplas
- Interface gráfica com Tkinter ou web com Flask

---

### 👨‍💻 Desenvolvido por:  
**João Vitor de Lima Sampaio**  
[LinkedIn](http://www.linkedin.com/in/jo%C3%A3o-vitor-de-lima-sampaio-1566a124a) | [GitHub](https://github.com/Joaovitorsamps?tab=repositories)
