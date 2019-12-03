# docker-webservice

Required setup. Nothing should be required other than docker and docker-compose.

Commands to start the docker compose files:

docker-compose -f docker-compose.yml up
docker-compose -f docker-compose-prod.yml up

----------------------------
FILES EXPLANATIONS

** server.py

a python script that accepts connection on port 8080
accepts a post and get on addTask and getTasks to add or get data
from mongodb database

** Dockerfile-db

docker file that starts from alpine, installs and starts mongodb

** Dockerfile-server

dockerfile for the server
simply install python and start the script

** Dockerfile-testclient

** client.sh

just alpine and curl. send some sample post data to the webservice and then GETs the tasks
