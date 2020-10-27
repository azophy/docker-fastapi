Docker FastAPI
==============

Experimental repo used to learn about Dockerfile, docker-compose, and FastAPI

## how to run

`docker run -it --name <container_name> -p "8000:80" "azophy/fastapi-example:latest"`

or using docker-compose file inside this project file

`docker-compose up`

## How to build and push

```
# dont forget the last '.' !!
docker build -t "azophy/fastapi-example:latest" . 
docker push "azophy/fastapi-example:latest"
```
