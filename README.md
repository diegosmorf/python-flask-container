# Python-Flask-Container 
This is a starting point (TEMPLATE) for REST API using python.

## Learning Path:
- [How to Add a Health Check to Your Docker Container](https://howchoo.com/devops/how-to-add-a-health-check-to-your-docker-container)
- [Python REST APIs With Flask, Connexion, and SQLAlchemy](https://realpython.com/flask-connexion-rest-api/)

## .Net Version
Python 3.8

## 3rd Party Nuget Packages 
- Python 3.8
- Flask
- Connexion
- Swagger

## Development Tools
 - Visual Studio Code
 - GIT Bash 
 - Swagger Editor  

## How to clone this project

```
cd\
mkdir python-flask-container
cd python-flask-container
git clone https://github.com/diegosmorf/python-flask-container.git
```

### Restore Libraries and run flask web server
```
pip install flask
pip install connexion
python main.py
```

### Create a docker image and RUN
```
docker build -t docker-flask .
docker run --rm --name docker-flask -p 5000:5000 docker-flask

```
You can access this Frontend via browser: http://localhost:5000 and the API via: http://localhost:5000/swagger
