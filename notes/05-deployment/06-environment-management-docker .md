# Environment Management: Docker

## Why we need docker
It is a way of managing environments one step above pipenv. It lets us isolate our service or, app from the rest in our development machine.

## Running a python image with docker
It is a docker image with just python, nothing else in it.

- Go to `hub.docker.com/_/python`. It contains all images of python. It shows all the tags.  

- Run a image from there with:

`$ docker run -it --rm python:3.8.12-slim`

or, better we ca go inside this image and do whatever we want with entrypoint.

`$ docker run -it --rm --entrypoint=bash python:3.8.12-slim`


## Dockerfile
Everything that we  want to do inside a docker image can be written in a Dockerfile. This is how Dockerfile looks like:

```Dokcerfile
FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]


RUN pipenv install --system --deploy

COPY ["predict.py", "model_C=1.0.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"] 

``` 


## Building a docker image

`$ docker build -t zoomcamp-test .`

`zoomcamp-test` is the tag name. I can use other tag e.g. `midterm-project`, `castone-project` etc.

## Running a docker image locally
We can run the above image like we did it previously with:

`$ docker run -it --rm -p 9696:9696 zoomcamp-test:latest`

When we run it we see that, we are inside /app. 

If there is a chnage we made into Dockerfile, then build it again and then you can run it. 
`$ docker run -it --rm -p 9696:9696 zoomcamp-test:latest`

