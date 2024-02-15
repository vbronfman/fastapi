 FastAPI with uvicorn example
#
# start with
#     uvicorn main:app  --reload --port=8080 --host=0.0.0.0
#     http://localhost:8080/docs to see swagger docs


1. activate virtual env

virtualenv fastapifolder

source env_name/bin/activate

2. save dependencies
   freeze > requirements.txt

   deactivate 


Dockerizing
save dependencies
freeze 

create Dockerfile
build
docker build .

docker image tag

Run container to upload environment file run as  . There is PORT variable in .env , but need to think out a way to set it for "publish"

docker run -d --env-file .env --publish 8080:8080 --restart unless-stopped vbronfman/fastapiexample


