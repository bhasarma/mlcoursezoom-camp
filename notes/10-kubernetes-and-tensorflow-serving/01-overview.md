## 10.1 Overview: kubernetes and tensorflow serving

In this module, we'll talk about kubernetes and tensorflow serving.

Scenarion: we have a user, who uploads an image of a pant e.g. into the website to sell it. We want to build a system that automatically classify what type of cloth user has uploaded. 

In this module, we'll use **tensorflow serving** for serving the model. This is a tool from the tensorflow family of tools, created specifically for serving tnesorflow models. 

In **Tensorflow Serving** we'll have the model trained already. Tensorflow serving is a library written in c++. It is very efficinet and focuses only on inference. It can't do anything else, but inference. 

X matrix of the image comes as input to TF-serving. Image is already prepared with preprocess_input fuction into a matrix with nupmy array. Output of TF-serving is a numpy array with 10 predictions. These are 10 different scores for 10 different classes. 

Our user can't have the image, preprocess it and convert it into an arraay. User will just upload the picture. Then to help the user, we'll have something called **GATEWAY** before TF-serving. Gateway will get anurl of the image as input and outputs in consumable format e.g. not just as an array, but json with class name. 

Our website, where image is uploaded talks to Gateway and just send the url of the pants. gateway will donload the image, process it and then will send it to TF-serving. For this a protocol called **grpc** is used. It os a special binary protocol that is very effective, very efficient. TF-serving uses it. Then TF-serving will reply back with a number. Gateway will process this number, convert it into humane readable predictions. Then send back the predicitons. Then website will use this prediction to suggest the category. 

For implementing the Gateway we'll use Flask. TF-serving uses C++. We don't have much control over it. We just have to use c++. Then we'll deploy everything, we created here to kubernetes.

It might seem little complicated because we have two components: first one Gateway and second one TF-serving. First of all it is necessity, because TF-serving expects input to be prepared. Secondly, there is an advanatage, for TF-serving we can use GPU. But for Gateway we can use a CPU. What Gateway is doing is downloading the images, resizes them. It turns this into umpy array. This is not very computationally expensive. 

But in TF-serving we are applying the model to the image. For this it is doing lots of matrix multiplication and things like that. These things can be run very fast on GPUs. But for a Gateway a cpu is enough. e.g. we can have 2 instances of TF-serving that will run on GPU and 5 instances of the Gateway that runs on CPUs. We can scale them independently, not to have lots of TF-serving instances, because it costs money to run on gpus. But for Gateway we don't need very powerful machines, but may be we need more of them. It is also useful to have such an architecture. We can scale these things indepnendentl. One more thing Gateway is doing is postprocessing the output. We already have code for that. This is something we did in the last session, when we used the model for aws lambda. We can reuse most of this code.

In this module, we'll mostly focus on creating these two services, deploying them and test them. 

![Imgur](https://i.imgur.com/ToRfjIn.png)
Figure 1: overview of Kubernetes and TF-serving

## 10.1 Overview
- what we'll cover this week
- two-tier architecture

## 10.2 Tensorflow serving
- the saved_model format
- running TF-serving locall with docker
- Invoking the model from jupyter

## 10.3 creating a preprocessing service
- converting the notebook into a python script
- wrapping the script into a Flask app

## 10.4 Running everything locally with Docker-compose
- preparing the images
- installing docker-compose
- running the service
- testing the service

## 10.5 Introduction to Kubernetes
- The anatomy of a Kubernetes cluster

## 10.6 Deploying a simple service to Kubernetes

- installing kubectl
- setting up a local Kubernetes cluster with Kind
- creating a deployment
- creating  a service

## 10.7 Deploying Tensorflow model to Kubernetes

- Deploying the TF-serving model
- Deploying the Gateway
- Testing the service

## 10.8 Deploying to EKS

- Creating a EKS cluster on AWS
- Publishing the image to ECR
- Configuring kubectl

## 10.9 Summary 
**References**

1. Youtube video [link](https://www.youtube.com/watch?v=mvPER7YfTkw&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=98) 