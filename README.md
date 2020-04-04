# Extremely simple WebApp

**Why make it so simple?**

1. The more complex the application the more platform specific issues are likely to occur 
2. We want to remove as many variables from the comparison as possible


The Program uses, 

- Python3.7 Alpine 
- Flask 
- Docker-Compose/Docker
- pytest


## How to Run in Deployment Script or locally

To Run the Application 

`docker-compose build`

`docker-compose up`

It will be running @ `http://0.0.0.0:5000/`


## How to run tests for Continous Integration

Given access to run script in the CI Platform, simply run this command. It returns -1 if tests fail, and 0 if it passes. 
 
 `$ pytest` 

