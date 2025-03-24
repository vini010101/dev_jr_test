# Usar uma imagem base com Python
FROM python:3.9-slim

# Atualizar e instalar as dependências necessárias para o SQLite e outras bibliotecas
RUN apt-get update && \
    apt-get install -y libsqlite3-dev gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar apenas os arquivos necessários para otimizar o cache de build
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do projeto
COPY . .

# Expor a porta que o FastAPI vai rodar
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
