# Instalación
#### Crea un virtual env dentro de la carpeta backend
python3 -m venv env
source env/bin/activate  # En windows usa `env\Scripts\activate`

#### Instala Django y Django REST y framework 
pip install django
pip install djangorestframework
#### instala los paquetes adicionales
pip install django-cors-headers
pip install djangorestframework_simplejwt
pip install Faker

## Iniciando la base de datos

Inicia la base de datos corriendo 

python manage.py migrate

Podras acceder a
http:localhost:8000

## Crea un super user
python manage.py createsuperuser

## Inicia el servidor para backend
python manage.py runserver

## Levanta el frontend
Dentro de la carpeta Frontend en consola ejecuta el comando 

npm install
npm run start

Esto levantara el servidor en el puerto 3000
http://localhost:3000

## Api Endpoints
#### POST Inicio de session
/api/login

#### GET Lista todos los vehiculos
/api/veichles
#### POST Crea un vehiculo
/api/vehicle
#### GET Detalles de un vehiculo
/api/vehicle/{id}
#### PATCH Actualiza un vehiculo
/api/vehicle/{id}/update
#### DELETE Elimina un vehiculo
/api/vehicle/{id}/delete





