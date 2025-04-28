FROM python:3.11

# Establecer el directorio de trabajo en el contenedor
WORKDIR /src

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias necesarias
RUN apt-get update && apt-get install -y python3-distutils

# Instalar las dependencias de Python
RUN pip install -r requirements.txt

# Copiar todo el contenido del directorio actual (desde el contexto de construcción) al directorio /src en el contenedor
COPY . .

# Ejecutar la aplicación
CMD ["python", "app.py"]
