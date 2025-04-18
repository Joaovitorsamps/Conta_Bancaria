# 💰 Desafio Inicial - Sistema Bancário em Python

## 📌 Objetivo Geral

Desenvolver um **sistema bancário simples**, via terminal, com as seguintes operações:

- **Depósito**
- **Saque**
- **Transferência**
- **Visualização de Extrato**

Esse projeto visa praticar lógica de programação, estrutura de repetição e controle de fluxo em Python.

---

## ⚙️ Funcionalidades

### ✅ Operação de Depósito
- Permite inserir qualquer valor maior que 0.
- Cada valor depositado é **armazenado** e exibido posteriormente na operação de **extrato**.

### ✅ Operação de Saque
- O sistema permite **3 saques diários**, com **reinício automático a cada dia**.
- Cada saque possui um limite de **R$ 500,00** por operação.
- Caso o valor exceda o saldo disponível, é exibida uma mensagem informando a **falta de saldo**.
- Todos os saques são **registrados e exibidos no extrato**.

### ✅ Operação de Transferência
- Permite realizar até **10 transferências por dia**, com controle diário de limite.
- Cada transferência é registrada no extrato com a data e valor.
- Não permite transferir valores negativos ou superiores ao saldo disponível.

### ✅ Operação de Extrato
- Exibe todos os depósitos, saques e transferências realizados.
- Mostra o **saldo atual** da conta no formato `R$ XXX.XX`.
- Caso nenhuma operação tenha sido feita, exibe uma mensagem de ausência de movimentações.

---

## 🧠 O que foi utilizado

- ✅ **Variáveis** (armazenamento de saldo, extrato, limites e contadores)
- ✅ **Laço de repetição** `while` (estrutura principal do menu)
- ✅ **Condicionais** `if`, `elif`, `else` (controle de fluxo)
- ✅ **Função** `input()` para entrada de dados
- ✅ **Formatação de strings** com `f-strings`
- ✅ **Manipulação de datas** com `datetime`
- ✅ **Controle de limite diário baseado na data atual**
- ✅ **Operadores aritméticos e lógicos**
- ✅ **Exibição de mensagens condicionais** com ternário (`if not extrato`)

---

## 📈 Curva de Aprendizado

Este desafio permitiu a aplicação prática de:

- 🧩 **Lógica condicional com múltiplos cenários** (valores inválidos, limite de saque, saldo insuficiente)
- 🔄 **Estrutura de repetição com controle de saída e reset diário de limites**
- 🧠 **Simulação de regras reais de um sistema bancário** (limites, datas, extratos)
- 🛠️ **Tratamento de entradas e validações simples** (valores negativos, tipos numéricos)
- 📅 **Controle de datas com `datetime` para operações financeiras**
- 💡 **Organização e clareza do código** para facilitar futuras expansões

---

## 🗃️ Código-fonte

Todo o código está contido no arquivo principal `sistema_bancario.py`. O sistema é executado inteiramente no terminal.

---

## 🚀 Próximos Passos (Sugestões de Evolução)

- Melhorar a modularização com funções
- Evoluir para **Programação Orientada a Objetos (POO)**
- Criar interface gráfica ou versão web
- Armazenar dados em arquivos ou banco de dados
- Adicionar autenticação de usuário (simples ou avançada)

---

### 👨‍💻 Desenvolvido por:  
**João Vitor de Lima Sampaio**  
[LinkedIn](http://www.linkedin.com/in/jo%C3%A3o-vitor-de-lima-sampaio-1566a124a) | [GitHub](https://github.com/Joaovitorsamps?tab=repositories)
