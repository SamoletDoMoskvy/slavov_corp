# slavov_corp

### REQUIREMENTS
* Docker
* Docker-compose

### INSTALLATION
```bash
git clone https://github.com/SamoletDoMoskvy/slavov_corp
cd slavov_corp
docker-compose up
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```
