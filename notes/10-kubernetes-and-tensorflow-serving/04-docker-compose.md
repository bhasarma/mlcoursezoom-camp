# 10.4 docker compose

- write my-image.dockerfile
- bult docker image with:
```
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ docker build -t zoomcamp-10-model:xception-v4-001 -f image-model.dockerfile .
```

output:
```
Sending build context to Docker daemon  175.9MB
Step 1/3 : FROM tensorflow/serving:2.7.0
 ---> e205cbd4dcb1
Step 2/3 : COPY clothing-model /models/clothing-model/1
 ---> 3d525d5be8c5
Step 3/3 : ENV MODEL_NAME="clothing-model"
 ---> Running in 17dad063c634
Removing intermediate container 17dad063c634
 ---> 6672176426df
Successfully built 6672176426df
Successfully tagged zoomcamp-10-model:xception-v4-001
```

Now let's create a new command for running it.
 We run:
 
 ```
 (base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ docker run -it --rm \
-p 8500:8500 \
zoomcamp-10-model:xception-v4-001 
 ```
In aother terminal we run:
```
pipenv run python gateway.py
```
We get the predictions.

Now we have an image for TF-serving model. Now its in docker. We built a docker image for that. Now we need to do the same for our gateway service. 

Now let's reate the file `image-gateway.dickerfile`. This content of this file can be directly copied from what we did in `Dockerfile` of module 05.  We save this file and then we'll build the docker image. 

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ docker build -t zoomcamp-10-gateway:001 -f image-gateway.dockerfile .
Sending build context to Docker daemon  175.9MB
Step 1/8 : FROM python:3.8.12-slim
 ---> 513da2530098
Step 2/8 : RUN pip install pipenv
 ---> Using cache
 ---> 7356dae8d4e6
Step 3/8 : WORKDIR /app
 ---> Using cache
 ---> 818d1de32c03
Step 4/8 : COPY ["Pipfile", "Pipfile.lock", "./"]
 ---> 851af70e9a6c
Step 5/8 : RUN pipenv install --system --deploy
 ---> Running in d9590fdb4725
Installing dependencies from Pipfile.lock (8b6147)...
Removing intermediate container d9590fdb4725
 ---> a2f6e87f2dfd
Step 6/8 : COPY ["gateway.py", "proto.py", "./"]
 ---> 4a1558e1dd79
Step 7/8 : EXPOSE 9696
 ---> Running in f925a0996457
Removing intermediate container f925a0996457
 ---> db71dea693df
Step 8/8 : ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "gateway:app"]
 ---> Running in 8d90c6034746
Removing intermediate container 8d90c6034746
 ---> a390325c7c56
Successfully built a390325c7c56
Successfully tagged zoomcamp-10-gateway:001
``` 
**In order to run TF-serving and Gateway-service in the same host machine, we need to put them in the same network**. Then they will be able to communicate with each other. We can use this using plain docker. But there is a nicer way to do this. 
The way of linking multiple docker services together is call docker-compose. Docker compose allows us to run multiple docker-containers and then link related ones to each other. All of them will run in a single network and it will be able to talk to each other, if needed. 

For using it we first need to install it.  


Done with installation and adding to path, now write docker-compose.yaml file.

Then do `docker-compose up`.

Now test it:

```
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ python test.py 
{'dress': -1.87986421585083, 'hat': -4.75631046295166, 'longsleeve': -2.359531879425049, 'outwear': -1.08926522731781, 'pants': 9.903782844543457, 'shirt': -2.826179027557373, 'shoes': -3.648310422897339, 'shorts': 3.241154909133911, 'skirt': -2.612096071243286, 't-shirt': -4.852035045623779}
```

We can also run our service in detached mode with `docker-compose up -d`.Then we also run our services, but we get back our terminal. 

- python test.py
- docker ps
- docker-compose down