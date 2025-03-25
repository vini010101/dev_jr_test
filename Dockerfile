# Usar uma imagem base com Python
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y libpq-dev gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /
# Copiar todo o código do projeto
COPY . .

# Copiar apenas os arquivos necessários para otimizar o cache de build
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt



# Expor a porta que o FastAPI vai rodar
EXPOSE 8000

# Comando para iniciar a API
CMD ["python", "-m", "uvicorn", "whater_api.app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
