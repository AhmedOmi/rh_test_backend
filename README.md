# rh_test_backend
### Clone the project
git clone https://github.com/AhmedOmi/rh_test_backend.git

### Go to project
```bash
cd rh_test_backend  
```

### run the project
```bash
sudo  docker-compose up  
```

### Create the database
### Make Migrations
```bash
 sudo docker-compose run app python manage.py makemigrations
```
```bash
 sudo docker-compose run app python manage.py migrate
```

### Create Super User
```bash
 sudo docker-compose run app python manage.py createsuperuser
```