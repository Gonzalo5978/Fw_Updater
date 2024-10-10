FROM python:3.13-alpine

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del programa al contenedor
COPY . .

# Instalar las dependencias si es necesario (comenta si no aplican)
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Especificar el comando de ejecución por defecto
CMD ["python", "src/run.py"]

ENTRYPOINT ["python", "src/run.py"]
