# slavov_corp

### REQUIREMENTS
* Docker
* Docker-compose

### INSTALLATION
Get the application
```bash
git clone https://github.com/SamoletDoMoskvy/slavov_corp
cd slavov_corp
```
Building the app & applying migrations
```bash
docker-compose up
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
```
Create a user for the application
```bash
docker-compose exec backend python manage.py createsuperuser
```
The application will be available at http://0.0.0.0/ \
The admin panel is available at http://0.0.0.0/admin (Use the username and password that you specified when creating the user) \
Create an instance of the model at this address http://0.0.0.0/admin/cargo_app/cargo/add/
Then you can go to the invoice using the button in the interface, or go to http://0.0.0.0/api/cargo/get_report/<ID>/
> ID is Cargo object (293105630202205141717498738223) in brackets. That's an example value.
