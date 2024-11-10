## Intrucciones para ejecutar y correr CatsDics

1. Descargamos conda
   [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
2. Creamos un entorno virtual.
```sh
$ conda env create -n CatsDics python=3.9
```
3. Activamos nuestro entorno de conda con:
```sh
$ conda activate CatsDics
```
4. Instala Django en el entorno recién creado
```sh
$ pip install django
```
6. Realiza las migraciones
```sh
$ python manage.py migrate
```
7. Inicia un nuevo proyecto de Django (este paso es opcional, pero ayuda a verificar que Django se ha instalado correctamente)
```sh
$ cd CatsDicsApp
$ python manage.py runserver
```
