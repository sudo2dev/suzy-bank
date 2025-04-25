# 💰 Suzy Bank

Projeto de um sistema bancário simples, desenvolvido em **Python**, com foco em aprendizado e prática de lógica de programação.

---

## 🧩 Funcionalidades - Versão 1

### 📥 Depósito
- Permite depósitos de valores **positivos**.
- Apenas um único usuário (não há sistema de autenticação).
- Todos os depósitos são registrados e exibidos no extrato.

### 💸 Saque
- Limite de até **3 saques por dia**.
- Valor máximo de **R$ 500,00 por saque**.
- Exibe mensagem de erro em caso de **saldo insuficiente**.
- Todos os saques são registrados e exibidos no extrato.

### 📄 Extrato
- Lista todos os **depósitos e saques** realizados.
- Mostra o **saldo final** da conta.
- Os valores são exibidos no formato: `R$ 000.00`.

### Todo
- Faltou exibir os valores no formato `R$ 000.00`.

🔗 Versão 1 disponível em:  
https://github.com/sudo2dev/suzy-bank/tree/feature/v1

---

## 🧩 Funcionalidades - Versão 2

Nesta versão foram adicionadas novas funcionalidades:

### 👤 Cadastro de Usuário
- Permite cadastrar clientes informando: **nome, data de nascimento, CPF e endereço**.
- O endereço deve seguir o formato:  
`logradouro, número - bairro - cidade/sigla do estado`.
- O sistema **impede o cadastro de usuários com CPF duplicado**.

### 🏦 Cadastro de Conta Bancária
- Permite criar contas bancárias associadas a um usuário.
- Cada conta possui:
  - **Agência:** valor fixo `0001`.
  - **Número da conta:** gerado automaticamente e de forma sequencial.
  - **Usuário vinculado:** cliente dono da conta.
- Um usuário pode ter **mais de uma conta bancária**.

### Todo
- Melhorar interface do usuário
   - Guardar a conta informada para não redigita-la a cada operação
   - Corrigir formatação para listar contas e lista usuários
- Melhorar código
   - Mudar para OO
   - Revisar exceções
- Melhorar testes
   - Melhorar uso de dados simulados
   - Melhorar os testes para usuarios e contas

🔗 Versão 2 disponível em:  
https://github.com/sudo2dev/suzy-bank/tree/feature/v2

---

## 🧩 Funcionalidades - Versão 3

- Versão orientada a objetos
- Ainda não aplica algumas restrições, como qtd de sacas no dia ou total.

🔗 Versão 4 disponível em:  
https://github.com/sudo2dev/suzy-bank/tree/feature/v4

---

## 🧩 Funcionalidades - Versão 4

- Pacote do projeto publicado no pypi

## ▶️ Como executar

1. Certifique-se de ter o **Python 3.8 ou superior** instalado.
2. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/suzy-bank.git
   cd suzy-bank
   ```
3. Ou instale via pypi
   ```bash
   pip install suzy-bank
```
3. Execute o sistema:
   ```bash
   python suzy_bank.py
   ```
4. Execute os testes:
   ```bash
   python -m tests.tests
   ```

---

💡 Projeto disponível em:  
https://github.com/sudo2dev/suzy-bank
