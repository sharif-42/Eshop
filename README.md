# Eshop

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/sharif-42/Style-Icon/graphs/commit-activity)
[![Maintainer](https://img.shields.io/badge/maintainer-Sharif_42-blue.svg)](https://github.com/sharif-42)

[![Generic badge](https://img.shields.io/badge/MadeWith-Python3.10-green.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/FrameWork-Django4-%230db7ed.svg)](https://docs.djangoproject.com/en/3.2/)
[![Generic badge](https://img.shields.io/badge/FrameWork-DjangoRestFrameWork-red.svg)](https://www.django-rest-framework.org/)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch)


Backend of Eshop. Eshop is an E-Commerce Site. Developed on Python3.10 and Django4. 
## Features
This BE is used for Both FE and Dashboard.
- ### Dashboard Features
    - User list
    - Product CRUD operation
    - Order List and Details
    - Lightweight Statistics.
- ### FE Features
  - User registration, Login, logout, update and role-based permissions and token based authentication
  - Product List and Details. 
  - Order Process 

## Run on docker
```commandline
docker-compose -f local.yml build
docker-compose -f local.yml up
docker-compose -f local.yml down
```
### Necessary Management Commands
  ```shell
  # Create new app
  docker-compose -f local.yml run django sh -c "python manage.py startapp <App_Name>"
  # Migration commands
  docker exec -it eshop_django_1 sh -c "python manage.py makemigrations"
  docker exec -it eshop_django_1 sh -c "python manage.py migrate"
  # Create super user
  docker exec -it eshop_django_1 sh -c "python manage.py createsuperuser"
  # Run shell
  docker exec -it eshop_django_1 sh -c "python manage.py shell_plus"
  ```
### Elastic Commands
  ```shell
  docker exec -it eshop_django_1 sh -c "python manage.py search_index --rebuild -f"  # Index everything.
  docker exec -it eshop_django_1 sh -c "python manage.py search_index --delete -f"   # Delete all index.
  ```