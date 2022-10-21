## 7.3 Deploying our prediction sevice

In last module, we looked at building our prediction service. We did that by saving ouu model, packaging it up and deploying it in a bento by creating the end point and then testing it. 

In this module we'll look at: 

- what BentoML is doing behind the scene
- we are going to build our Bento 
- we are going to see all the dependencies and the things that are brought in automatically.
- Then we are going to build a docker container and run it.

First:
1. One of the things that BentoML provides is the command line tool. This can be used to look at the stuffs that we have saved, Bentos that we have built.

```
$ bentoml models list
```

gives the list of models that we have saved as output a shown below: 

```
 Tag                                 Module           Size        Creation Time       
 credit_risk_model:bubbpqsqmscgpf2d  bentoml.xgboost  197.77 KiB  2022-10-20 12:43:36 
 credit_risk_model:bryqeucqmscgpf2d  bentoml.xgboost  197.07 KiB  2022-10-20 12:43:35 
 credit_risk_model:ztgcukspx6livn6r  bentoml.xgboost  197.77 KiB  2022-10-19 17:07:51 
 credit_risk_model:waipffspxclivn6r  bentoml.xgboost  197.07 KiB  2022-10-19 16:16:56 

```


What has automatically saved for us inside a model can be obtained by:

```
$ bentoml models get credit_risk_model:bubbpqsqmscgpf2d
```

as output for the above command we get:

```
name: credit_risk_model                                                                                                                                                                           
version: bubbpqsqmscgpf2d                                                                                                                                                                                    
module: bentoml.xgboost                                                                                                                                                                                      
labels: {}                                                                                                                                                                                                   
options:                                                                                                                                                                                                     
  model_class: Booster                                                                                                                                                                                       
metadata: {}                                                                                                                                                                                                 
context:                                                                                                                                                                                                     
  framework_name: xgboost                                                                                                                                                                                    
  framework_versions:                                                                                                                                                                                        
    xgboost: 1.6.2                                                                                                                                                                                           
  bentoml_version: 1.0.7                                                                                                                                                                                     
  python_version: 3.9.13                                                                                                                                                                                     
signatures:                                                                                                                                                                                                  
  predict:                                                                                                                                                                                                   
    batchable: false                                                                                                                                                                                         
api_version: v2                                                                                                                                                                                              
creation_time: '2022-10-20T10:43:36.355254+00:00'  
```

We see above we have got name and tag in the framework. We have also got version of the framework: version of BentoML and python version. It is important to save the framework version, because when we are recreating the model, when we are loading it in our Bento later, it needs to be with the exact same framework that we use when we are training. Otherwise we may get inconsistent results. It is nice to use the same python and other version if possible, although it depends on the particular service. In module 5 also we looked at what version we are using and we configured that in our pip file manually. Bentoml automatically determine what version the model was saved with and autmatically pulls in that depenndency, so that we don't have to worry about it. 

2.Now we are going to see how to build our Bento.
We have got all the information above. We want to build our single unit deployable. The way that Bento build is using a `bentofile.yaml`. It is a preety standard Bento file.  You can have a look at the file in github repo.

Once we have got our `service.py`and `bentofile.yaml`, we can build our bento. For this we'll write on terminal: 
```
$ bentoml build
```
It is going to locate our service file, pull the model that are in there, look at the bentofile and pull in all the right dependencies and create one single deployable for us. 

Output of Bentoml Build is:

```

Building BentoML service "credit_risk_classifier:km46shsqscdii5ms" from build context "/home/bsarma/GitHub/mlcoursezoom-camp/WK07-BentoML-production-ready-ML"
Packing model "credit_risk_model:bubbpqsqmscgpf2d"
Locking PyPI package versions..

██████╗░███████╗███╗░░██╗████████╗░█████╗░███╗░░░███╗██╗░░░░░
██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗████╗░████║██║░░░░░
██████╦╝█████╗░░██╔██╗██║░░░██║░░░██║░░██║██╔████╔██║██║░░░░░
██╔══██╗██╔══╝░░██║╚████║░░░██║░░░██║░░██║██║╚██╔╝██║██║░░░░░
██████╦╝███████╗██║░╚███║░░░██║░░░╚█████╔╝██║░╚═╝░██║███████╗
╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

Successfully built Bento(tag="credit_risk_classifier:km46shsqscdii5ms")

```
Also you can look at [here](https://twitter.com/ML_BSarma/status/1583127130392604673)


Now we'll go to
```
(bentoml) bsarma@bsarma-Inspiron-5370:~/bentoml/bentos/credit_risk_classifier/km46shsqscdii5ms$
``` 
and goona look at everything that is saved there with
```
$ tree
```

and this is how it looks like:

```
├── apis
│   └── openapi.yaml
├── bento.yaml
├── env
│   ├── docker
│   │   ├── Dockerfile
│   │   └── entrypoint.sh
│   └── python
│       ├── install.sh
│       ├── requirements.lock.txt
│       ├── requirements.txt
│       └── version.txt
├── models
│   └── credit_risk_model
│       ├── bubbpqsqmscgpf2d
│       │   ├── custom_objects.pkl
│       │   ├── model.yaml
│       │   └── saved_model.ubj
│       └── latest
├── README.md
└── src
    ├── data_test.py
    └── service.py

8 directories, 15 files

```
Now we are going to build the docker image with the following command:

```
(bentoml) bsarma@bsarma-Inspiron-5370:~/GitHub/mlcoursezoom-camp/WK07-BentoML-production-ready-ML$ bentoml containerize credit_risk_classifier:km46shsqscdii5ms
```
But it showed the following error:

```
Error: [bentoml-cli] `containerize` failed: BentoML requires BuildKit (via Docker Buildx) to be installed to support multi-arch builds. Buildx comes with Docker Desktop, but one can also install it manually by following instructions via https://docs.docker.com/buildx/working-with-buildx/#install.

```
I think I should install docker in `bentoml``env.  as instructed in MLZOOMCAMP with command:

```
sudo apt-get install docker.io
```
It was already installed. Thus it means that docker installation is not specific to env. I installed docker in module 5, not in bentoml env. Yet it is recognised. 

Even after installing docker.io I got the same error.

Then I installed Docker Desktop following the following [video](https://www.youtube.com/watch?v=Vplj9b0L_1Y)  . It worked till miniute 2:20 of the video. However I couldn't install Docker Desktop itself. Docker engine installation was fine. When I do `sudo apt install ./docker-desktop-4.13.0-amd64.deb` it gave me some error like `file doesn't exist`.  So I couldn't open docker desktop from ubuntu application menu.

I tried running bentml contaainerize command and I got now docker permission denied error, which I know that it is a sudo thing. Then I followed this [link](https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket). 

After this link I no longer needed to type sudo before docker. Now I tried `$ bentoml containerize credit_risk_classifier:km46shsqscdii5ms` and it worked perfectly. I got this error yesterday afternoon and today at 14:00 hour I resolved this small issue.

**Docker image is built**.  

We can look at the list of docker images built with:
```
$ docker images
```
Now we have our docker images, so we can run:
```
$ docker run -it --rm -p 3000:3000 credit_risk_classifier:km46shsqscdii5ms
```
Then we can go to `http://localhost:3000` and execute the bento before.

We got our container running. We have deployed our docker container `credit_risk_classifier:km46shsqscdii5ms`. This is eaxctly what we had, when we were serving directly from the code. This is the way we are going to be able to test it, as we continue to deploy.

End of video 7.3

**References:**
1. ML Zoomcamp 7.3 - Deploying Your Prediction Service [youtube link](https://www.youtube.com/watch?v=qpjLm_Lm4FA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=69)
