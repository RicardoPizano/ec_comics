# EC_MSCOMICS

## Descripción

Siguiendo los lineamientos antes mencionados, en esta primera parte se buscará crear un microservicio enfocado en la
búsqueda, dicho microservicio deberá de ser alimentado a partir de la API proporcionada, y deberá de satisfacer las
siguientes necesidades:

- CA1: Los usuarios tendrán la posibilidad de realizar una búsqueda por medio de una palabra (personajes y comics).
- CA2: En caso de no recibir un término de búsqueda, los usuario podrán acceder los personajes de la A a la Z.
- CA3: Los usuarios tendrán la posibilidad de agregar un filtro en caso de querer buscar específicamente un personaje o
  un comic.

## Requerimientos

- [python 3.9 o mayor](https://www.python.org/)

## Instalación

### Local

#### virtualenv (Opcional)

instalar virtualenv

``` bash 
$ pip3 install virtualenv 
``` 

crear virtualenv

``` bash 
$ virtualenv venv 
``` 

activar virtualenv

- linux

``` bash 
$ ./venv/bin/activate
``` 

- windows

``` bash 
$ ./venv/Scripts/activate
``` 

#### Dependencias

instalacion de dependencias

``` bash 
$ pip3 install -r requirements.tx
``` 

#### Ejecutar

``` bash 
$ python3 main.py
``` 

### Docker

#### Descargar imagen

``` bash
$ docker pull ec_mscomic:latest
```

#### Crear contenedor

``` bash
$ docker run -d -p --name container_ec_msusers ${puerto}:80 ec_mscomics 
```