# FROM python:3.8-slim-buster
FROM python:3.8-alpine

COPY . /app
WORKDIR /app

# RUN apt-get update -y 
# RUN apt-get install -y python
# RUN apt-get install -y python-pip
#RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install flask
RUN pip install connexion

HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1
CMD ["python", "main.py"]