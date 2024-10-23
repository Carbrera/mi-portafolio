* crear carpeta

* crear entorno virtual
python -m venv .venv

* activar entorno virtual
.venv\Scripts\activate.ps1

* instalar django en el entorno si no existe
pip install Django==5.1.2

* crear proyecto
django-admin startproject nombre_proyecto

* crear app dentro del proyecto
django-admin startapp nombre_app

* registrar cada app en el archivo ettings.py que se encuentra dentro de la carpeta del proyecto
INSTALLED_APPS = [
    'nombre_app.apps.AppConfig',
]
* migrar los cambios a la base de datos
python manage.py migrate

* inicializar el servidor
python manage.py runserver

* terminbar el servidor
ctrl + c

* verificacion e instalacion de python
python --version

* verificacion de pip
pip --version

* verificacion e instalacion de virtualenvwrapper
pip install virtualenvwrapper

