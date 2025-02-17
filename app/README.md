# Sistema de Gestão de Eventos

## 📌 Sobre o Projeto
O **Sistema de Gestão de Eventos** é uma plataforma web desenvolvida para facilitar o gerenciamento de eventos, permitindo o cadastro de eventos, gerenciamento de participantes e palestrantes, e controle de inscrições.

## 🚀 Tecnologias Utilizadas
- **Backend:** FastAPI + SQLAlchemy + PostgreSQL
- **Autenticação:** JWT (JSON Web Tokens)
- **Frontend:** React + TypeScript + TailwindCSS
- **Testes:** Pytest
- **Banco de Dados:** PostgreSQL

## 📂 Estrutura de Pastas
```bash
event-system/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── database.py
│   ├── schemas/
├── tests/
├── .env
├── requirements.txt
├── README.md
```

## 🛠️ Como Instalar e Rodar o Projeto
### **1. Clonar o repositório**
```sh
git clone https://github.com/seu-usuario/event-system.git
cd event-system
```

### **2. Criar um ambiente virtual e instalar dependências**
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### **3. Configurar variáveis de ambiente**
Crie um arquivo `.env` e adicione suas configurações, como credenciais do banco de dados.

### **4. Rodar a aplicação**
```sh
uvicorn app.main:app --reload
```
A API estará disponível em **http://127.0.0.1:8000**.

## 📅 Roadmap de Desenvolvimento
- ✅ Configuração do ambiente
- ⏳ Implementação do CRUD de eventos
- ⏳ Sistema de autenticação
- ⏳ Registro de participantes
- ⏳ Testes e documentação
- ⏳ Deploy


