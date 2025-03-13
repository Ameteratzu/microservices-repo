# Usar Python como base
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del microservicio
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
