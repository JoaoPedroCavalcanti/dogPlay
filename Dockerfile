# Usando a imagem oficial do python
FROM python:3.9-slim

# Definir o diretorio principal
WORKDIR /dogPlay

# Copiar o restante do projeto
COPY . .

# Copiar e instalar dependências do projeto
COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]