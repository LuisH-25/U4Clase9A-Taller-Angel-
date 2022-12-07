### Taller: Paginacion
Se realizo vistas basadas en clases y basadas en funciones, el unico cambio es en el html
en clase se tiene dos objetos que entran al html:   object_list y page_obj
en funciones se tiene un solo objeto:   page_obj

## Pasos para realizar todo la solucion

virtualenv env
source e s a	: para activar
pip install -r requirements.txt

# crear un proyecto y una aplicacion
django-admin startproject principal .
django-admin startapp libros

# agregar 
INSTALLED_APPS = [
    'libros',   # Se agrega cuando creo un app nuevo
]

# Cargar data de un json
python manage.py loaddata books.json

# Correr el proyecto
python manage.py runserver

# Para ver la paginacion 
http://127.0.0.1:8000/libros/?page=2


