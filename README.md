# 💰 Sistema Bancário em Python (Versão Orientada a Objetos com Autenticação e JSON)

## 📌 Objetivo Geral

Desenvolver um **sistema bancário via terminal**, com múltiplos usuários, autenticação com **CPF e senha**, e persistência dos dados usando arquivos `.json`, utilizando conceitos de **Programação Orientada a Objetos (POO)**, como encapsulamento, herança e classes abstratas.

Este projeto visa reforçar habilidades em design orientado a objetos, organização de código, controle de fluxo, e manipulação de arquivos e dados com Python.

---

## ⚙️ Funcionalidades

### ✅ Login e Cadastro de Usuário
- Login via **CPF e senha** com validação.
- Cadastro com verificação de duplicidade de CPF.
- Dados persistidos em `usuarios.json`.

### ✅ Depósito
- Permite depósitos com valores válidos.
- Atualiza saldo e registra a transação no extrato.
- Histórico salvo em `transacoes.json`.

### ✅ Saque
- Até **3 saques por dia**, com reinício automático a cada novo dia.
- Valor máximo por saque: **R$ 500,00**.
- Garante saldo suficiente antes de concluir.
- Todas as operações são registradas.

### ✅ Transferência
- Limite de **10 transferências por dia**.
- Verifica saldo e validade do valor.
- Registro automático no extrato com data e hora.

### ✅ Extrato
- Mostra o histórico completo de transações.
- Exibe o **saldo atual**.
- Caso não haja movimentações, informa a ausência de extrato.

### ✅ Listagem de Usuários
- Lista todos os usuários cadastrados no formato:
  ```
  Usuário: CPF - Conta: X - Agência: 0001
  ```

---

## 🧱 Arquitetura do Código (POO)

- `ContaBase` (abstrata): define a interface para saques, depósitos, transferências e extrato.
- `Conta`: implementação concreta da conta bancária, com controle de saldo, limites e extrato.
- `Usuario`: representa o cliente com CPF, senha e uma conta associada.
- `Banco`: gerencia usuários, autenticação, e interação com o sistema.
- `@property`: utilizado para proteger atributos sensíveis como `saldo`.
- `abc`: utilizado para forçar implementação de métodos essenciais em subclasses.

---

## 🛠️ Tecnologias e Recursos Usados

- `input()` e `print()` com formatação via `f-strings`
- `json` para manipulação de dados persistentes
- `os.path.exists()` para verificar existência de arquivos
- `datetime` para controle de datas e limites diários
- `textwrap.dedent` para formatação do menu
- `abc` (Abstract Base Class) para estruturar regras de negócio
- `@property` para encapsulamento e validação de atributos

---

## 📁 Estrutura de Arquivos

```
Conta_Bancaria/
│
├── usuarios.json            # Cadastro de usuários (CPF e senha)
├── transacoes.json          # Histórico de transações
└── banco_poo_refatorado.py  # Código principal com POO, abc e property
```

---

## 🚀 Próximos Passos (Melhorias Sugeridas)

- Associar número único de conta e agência por usuário
- Manter transações separadas por usuário
- Implementar **criptografia de senhas** com `bcrypt`
- Criar interface gráfica com `Tkinter` ou versão web com `Flask`
- Integrar com banco de dados (ex: SQLite, PostgreSQL)
- Adicionar testes unitários com `unittest` ou `pytest`
- Internacionalizar (i18n) e aplicar logs com `logging`

---

### 👨‍💻 Desenvolvido por:  
**João Vitor de Lima Sampaio**  
[LinkedIn](http://www.linkedin.com/in/jo%C3%A3o-vitor-de-lima-sampaio-1566a124a) | [GitHub](https://github.com/Joaovitorsamps?tab=repositories)