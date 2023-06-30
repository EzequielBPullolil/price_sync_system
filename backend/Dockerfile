# Usamos la imagen base de Python
FROM python:3.9.6

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos de la aplicación
COPY . /app

# Instalamos las dependencias de la aplicación
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install --no-cache-dir gunicorn flask

# Configuramos Nginx
RUN apt-get update
RUN apt-get install -y nginx

# Copiamos la configuración de Nginx
COPY nginx.conf /etc/nginx/sites-available/default

# Exponemos el puerto 80 para Nginx
EXPOSE 80

ENV PYTHONPATH="."
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh


# Definimos el comando de arranque
CMD ["/app/start.sh"]
