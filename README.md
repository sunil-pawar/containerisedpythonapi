# containerisedpythonapi
repository of docker container for python rest api to create add user and display users from mysql  

the repository contains REST API source code built using python call "app" a. includes dockerfile to build an Flask API to run as a docker container b. Source code to used to build docker image
Also it contains a folder for mysql related files and dockerfile to build and create a MYSQL 5.7 imaage with clients database and users to be created
Docker-compose file to build and run the docker images two docker containers
github action to remotely do the CD
whenever the master branch is pushed github action is triggered to build the docker image and run the docker on oracle cloud VM instance.
to the url by logging in to the OCI vm host and run the "curl -v http://localhost:8080/emp" to fetch the epmloyees data
run on the OCI VM host "curl -d curl -d @add.json -H "Content-Type: application/json" http://127.0.0.1:8080/add by keeping the add.json file on the pwd .
