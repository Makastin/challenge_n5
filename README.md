# Funcionalidades del Backend

## Estructura del Proyecto
Las ideas principal del proyecto es crear una plataforma que permita `Automatizar el Registro de Infarcciones de Transito`,
para los Oficiales a lo largo de periodo de trabajo.

La forma en la que estaestructurado el proyecto, permite la rapida emision de infracciones a usuarios que no cumplan
las normas de transito previamente existentes, asignandole un numero de infraccion unico y permitir obtener luego todas 
las infracciones asociadas a un usuario, filtrando mediante correo.

## Archivos/Estructura de archivos

El proyecto esta estructurado en una diversidad minima de apps que, pemriten ejercer de forma organizada
los requerimientos que se plantean dentro del desarrollo. Estas apps son:

- person
- vehicle
- officer
- core
- infringment

Cada una de las apps, contienen archivos de configuracion que son:

- models.py
- views.py
- forms.py
- urls.py

Los cuales contienen las configuraciones respectivas
Cada una de las apps mencionadas, ejercen un proceso distinto y unico dentro el proyecto, en caso contratio de la
app `core`, la cual mantiene la configracion completa del proyecto y se divide de la siguiente forma:

- wsgi.py
- asgi.py
- settings.py
- urls.py


## Ejecucion y funcionamiento del proyecto

El proyecto esta configurado para funcionar en un contenedor de `docker`

Ejecuta el siguente comandos:

```bash
$ docker-compose up
```

Mediante ese comando se ejecera la instalacion de todas las dependencias necesarias para hacer funcionar el proyecto



## Usuarios, accesos, procesos

El acceso al proyecto, esta planteado solo para acceder para personar que sean adminitradores dentro del mismo, no cuenta
con un modulo desarrollado de manejo de usuarios a clientes. Se utiliza el modelo de usuarios por defecto que implementa Django.

Por defecto al hacer funcionar el proyecto, se crean las siguientes credenciales:

- usuario: admin@localhost.com
- correo: admin@localhost.com
- contraseña: 4321Admin

## Testing

Para el proyecto se utiliza [`pytest`](https://docs.pytest.org/en/latest/) con
 [`pytest-django`](https://pytest-django.readthedocs.io/en/latest/), Python/Django UnitTest esta deshabilitado.


## Manejo de paquetes

Para el proyecto se usa [`Pipenv`](https://docs.pipenv.org/en/latest/).

## Antes de ejercer algun commit

Ejecuta los siguentes comandos:

```bash
$ isort . -m 3 -l 120
$ flake8
```

# API

## Descripcion

Dentro de la plataforma, se encuentran rutas o endpoints desarrollados, que permiten un facil acceso a la creacion de infracciones,
y facilitar la integracion de dichos servicios en otros entornos que contribuyan en agilizar las actividades laborales de oficiales.

Las rutas creadas para ser consumidas, se encuentran dentro de las rutas inicializadas como `http://127.0.0.1:8000/api/v1.0/`, tiendo que encuenta que la ruta `IP:PUERTO`  mencioandas,
son para uso local.

Las tutas que pueden acceder son:

## Obtener token de accceso


- `token/`

Esta ruta permite obtener un token asociado a un usuario registrado dentro de la plataforma, para luego ejercer ejecuciones dentro de los otras rutas

Cabe destacar que el tipo de autenticacion requerida es usuario y clave, la cual se ejerce con parametos `JSON` de la siguiente forma:
```
{
    "username":"admin@localhost.com",
    "password":"4321Admin"
}
```

Obteniendo como respuesta lo siguiente:
```
{
    "token": "8a6bfa444d23539cc3a44121b4fd3d429d90d34f"
}
````


## Creacion de Infracciones

- `infringement-create/`

Esta ruta es donde permite la creacion de infracciones dentro de la plataforma, es una ruta que amerita `Token de Autenticacion`, el cual se puede obtener den la ruta anteior.

Los parametos `JSON` que acepta la ruta, son los siguientes:

```
{
    "placa_patente":"l4pL4c4",
    "timestamp":"2023-02-17 15:00:00",
    "comentarios":"texto libre"
}
```

Cabe destacar que el tipo de autenticacion permitida dentro del header es `Bearer`

La respuesta obtenida es la siguiente:


```
{
    "data": {
        "status": 201,
        "numero_infraccion": "852c4a69-fb9a-4ba4-abfb-c0c98ee2afea",
        "oficial_asignado": "Marcos Castellanos"
    }
}
```

## Consulta de infracciones


- `infringement-search/`

Esta ruta permite la obtencion de todas infracciones cargadas a un usuario registrado dentro de la plataforma. Los parametos `JSON` que acepta la ruta, son los siguientes:

```
{
    "email":"correo@dominio.com",
}
```

Cabe destacar que el tipo de autenticacion no es necesaria para esta consulta

La respuesta obtenida es la siguiente:


```
{
    "status": 200,
    "data": {
        "multas": [
            {
                "fecha_multa": "2023-02-17T21:57:26.178037Z",
                "numero_multa": "9f661a55-9596-4ca9-8bec-6aacfe6be683",
                "oficial_asignado": "Marcos Castellanos"
            },
            {
                "fecha_multa": "2023-02-17T15:00:00Z",
                "numero_multa": "b7c4371a-3e64-4b20-85f9-ac337ca20139",
                "oficial_asignado": "Marcos Castellanos"
            },
            {
                "fecha_multa": "2023-02-17T15:00:00Z",
                "numero_multa": "852c4a69-fb9a-4ba4-abfb-c0c98ee2afea",
                "oficial_asignado": "Marcos Castellanos"
            }
        ]
    }
}
```



## Postman

Dentro de los arhivos se adjunta el `Postman Collections`, que contiene las rutas o endpoints desarrollados para ser utilizados por la platadorma
