# ⚡ TaskFlow — Squad Board

> Gerencie as tarefas da sua equipe em um board Kanban visual, simples e eficiente.

[![CI - Docker Build](https://github.com/anytaqueiroz/taskflow/actions/workflows/ci.yml/badge.svg)](https://github.com/anytaqueiroz/taskflow/actions/workflows/ci.yml)

---

## 📋 Descrição

**TaskFlow** é uma aplicação web de gerenciamento de tarefas no estilo Kanban. Ela permite que equipes organizem suas atividades em três colunas: **A Fazer**, **Em Progresso** e **Concluído** — facilitando a visualização do fluxo de trabalho da squad.

O projeto foi desenvolvido como parte da disciplina de DevOps, aplicando práticas modernas de ciclo de vida de desenvolvimento de software.

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python 3.12 + Flask 3.0 |
| Banco de Dados | SQLite (via Flask-SQLAlchemy) |
| Frontend | HTML5 + CSS3 + JavaScript |
| Servidor | Gunicorn |
| Containerização | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| Versionamento | Git + GitHub |

---

## 🚀 Guia de Instalação

### Pré-requisitos
- [Docker](https://www.docker.com/) instalado na máquina

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd taskflow
```

**2. Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o .env e defina uma SECRET_KEY segura
```

**3. Suba a aplicação com Docker**
```bash
docker compose up --build
```

**4. Acesse no navegador**
```
http://localhost:5000
```

### Para parar a aplicação
```bash
docker compose down
```

---

## 🗂️ Estrutura do Projeto

```
taskflow/
├── backend/
│   ├── app.py              # Aplicação Flask (rotas e modelos)
│   └── requirements.txt    # Dependências Python
├── frontend/
│   ├── templates/
│   │   └── index.html      # Interface principal
│   └── static/
│       ├── css/style.css   # Estilos
│       └── js/main.js      # Interações
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline CI/CD
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── .env.example            # Modelo de variáveis de ambiente
└── README.md
```

---

## 👥 Membros do grupo

| Nome | Matricula|
|------|--------|
| [Anyta da silva queiroz] | [01706122] |
| [Mariaa biatriz ramos rodrigues] | [01717058] |


---

## ✅ Critérios DevOps atendidos

- [x] Repositório Git com histórico de commits por todos os membros
- [x] Arquivo `.gitignore` configurado (sem `venv/`, `*.db`, `.env`)
- [x] Variáveis sensíveis via `.env` (nunca no código)
- [x] `Dockerfile` otimizado com imagem slim
- [x] `docker-compose.yml` para execução simplificada
- [x] Pipeline GitHub Actions com `docker build` automático a cada push
- [x] Selo "Passing" nas Actions do repositório
