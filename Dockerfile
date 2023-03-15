#IMG de python que usamos
FROM python:3.11

# Para poder leer los msjs de la propia consola y ejecución
ENV PYTHONUNBUFFERED 1 

#Directorio donde trabajaremos
RUN mkdir /code

#Nuestro directorio de trabajo
WORKDIR /code

#Nuestras dependencias (en este caso django)
COPY requirements.txt /code/

# python -m para utilizar la misma version de pip de la imagen de python
RUN python -m pip install -r requirements.txt

COPY . /code/