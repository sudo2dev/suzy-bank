# 💰 Suzy Bank

Projeto de um sistema bancário simples, implementado em **Python**, para fins de aprendizado.

---

## 🧩 Funcionalidades

### 📥 Depósito
- Permite depósitos de valores **positivos**.
- Apenas um único usuário (sem sistema de autenticação).
- Todos os depósitos são registrados e aparecem no extrato.

### 💸 Saque
- Limite de **3 saques por dia**.
- Valor máximo de **R$ 500,00 por saque**.
- Mensagem de erro em caso de **saldo insuficiente**.
- Todos os saques são registrados e aparecem no extrato.

### 📄 Extrato
- Lista todos os **depósitos e saques** realizados.
- Mostra o **saldo final** da conta.
- Os valores são exibidos no formato: `R$ 000.00`.

---

## ▶️ Como executar

1. Certifique-se de ter o **Python 3.10+** instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/suzy-bank.git
   cd suzy-bank
   ```
3. Para rodar o banco:
   ```bash
   python suzy_bank.py
   ```
4. Para rodar os testes:
   ```bash
   python tests.py
   ```

---

Disponível em: https://github.com/sudo2dev/suzy-bank