####### Creacion de un proyecto en django

1.- Crear una carpeta que almacene el proyecto
    ```
    dirigirse a la carpeta creada y abrirla en la terminal
    ```
2.- Crear entorno local
    ```
    python -m venv .venv
    ```
3.- Activar el entorno local o utilizar el entorno global existente cuando se instala python
    ```
    .venv\Scripts\activate.ps1
    ```
4.- Instalar django en el entorno, si esta instalado no es necesario
    ```
    pip list, para ver si está instalado
    python.exe -m pip install --upgrade pip, para actualizar el pip
    pip install django, para instalar django en el entorno
    ```
5.- Inicializar proyecto en django dentro de la carpeta creada en el primer paso
    ```
    django-admin startproject site_django
    django-admin startproject nombre_proyecto
    ```
6.- Ingresar a la carpeta del proyecto creado con django-admin startproject
    ```
    cd nombre_proyecto
    django-admin startapp book
    ```
7.- Modificar el archivo settings.py en el proyecto para registrar el aplicativo o app creada en el punto 6, con django-admin startapp
    ```
    INSTALED_APPS = [
    'book.apps.BookConfig', # agregando la app book al registro de aplicaciones instaladas
    ]
    ```
8.- Ejecutar migraciones
    ```
    python manage.py migrate
    python .\manage.py migrate # si no está en la misma carpeta
    ```
9.- Ejecutar el servidor local para verificar que todo esté correcto
    > dirigirnos a donde se encuentra el archivo manage.py dentro del proyecto
    ```
    python manage.py runserver
    python .\manage.py runserver # si no está en la misma carpeta
    ```
10.- Buscar ayuda sobre los comandos que podemos ejecutar con python manage.py
    ```
    python manage.py help