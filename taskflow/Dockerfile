# Imagem base leve
FROM python:3.12-slim

# Diretório de trabalho
WORKDIR /app

# Instalar dependências primeiro (camada cacheável)
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Porta exposta
EXPOSE 5000

# Variáveis de ambiente padrão
ENV FLASK_APP=backend/app.py
ENV FLASK_DEBUG=false

# Rodar com gunicorn (produção)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--chdir", "backend", "app:app"]
