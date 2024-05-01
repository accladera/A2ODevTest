FROM python:3.10.4-alpine3.15
LABEL authors="accladeram"
# Para mostrar logs
ENV PYTHONUNBUFFERED=1
# Indica que se trabajara en esa carpeta
WORKDIR /app

# Actualizar la distribucion,
# instalacion de compilador de toda la familia C,
# instalacion de base de datos,
# instalacion de python libs de desarrollo
# actualiza pip
RUN apk update\
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

# Copiamos los archivos del mi computadora al contenedor
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# desde el directorio de mi maquina ./ copia al directorio de mi contenedor ./
COPY ./ ./

# comando para correr el servidor en el contenedor, indicando la ip y puerto
CMD ["python","manage.py","runserver","0.0.0.0:8000"]





