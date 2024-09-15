# Etapa 1: Imagem base
FROM python:3.9-slim-buster

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de requisitos
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY app/ ./app/
COPY data/ ./data/

# Copiar o arquivo de variáveis de ambiente
COPY .env ./

# Expor a porta que a aplicação irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação, para desenvolvimento "--reload"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
