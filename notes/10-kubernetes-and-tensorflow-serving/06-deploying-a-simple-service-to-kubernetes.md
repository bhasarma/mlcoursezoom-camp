# 10.5 Deploying a simple service to kubernetes

We want to do a simple ping-pong application, that we did in module 5, using kubernetes. 

- create a new folder called `ping` in week-13 module, where we'll have the service
- copy `ping.py` from week 5 module

- go inside `ping folder

- do `touch Pipfile` 

- create a virtual env pipenv inside ping folder `pipenv install flask gunicorn`

Now we need a docker file for this application. Go to session 5 again and get the docker file from there, do the minor chanegs needed. 

Then,

```
docker build -t ping:v001 .
```
Run it with:

```
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ docker run -it --rm -p 9696:9696 ping:v001
```

- go to another terminal and do a curl request to 9696 with:

```
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ curl localhost:9696/ping
PONG
```

So that was our application. We sucessfully built it and run it.

Next step, we want to deploy it to kubernetes. 

For that we need to install a couple of things.

First we need to set up a local kubernetes cluster with kind. Kind is a special tool that allows to set up local kubernetes cluster. 

**Kubectl** is a tool for interacting with any kubernetes cluster. Let's first install kubectl.

## 10.5.1. Installing kubectl
 Link: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
 
 Or from aws since we are going to use AWS EKS later:
 
 https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
 
 ## 10.5.2 Installing kubectl
- refer to homework.md

## 10.5.2 Setting up a local kubernetes cluster with kind

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl get pod
No resources found in default namespace.

(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl get ddeployment
error: the server doesn't have a resource type "ddeployment"
```

Since these commands work, it mean that we  successfully installed kubectl and kind.

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED             STATUS             PORTS                                       NAMES
447716704f2a   kindest/node:v1.25.3   "/usr/local/bin/entr…"   9 minutes ago       Up 9 minutes       127.0.0.1:40183->6443/tcp                   kind-control-plane
0905e82b9f0d   ping:v001              "gunicorn --bind=0.0…"   About an hour ago   Up About an hour   0.0.0.0:9696->9696/tcp, :::9696->9696/tcp   sharp_cartwright
```
## 10.5.3 Creating a deployment

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl apply -f deployment.yaml
deployment.apps/ping-deployment created

(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl get deployment
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
ping-deployment   0/1     1            0           7m1s

(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl get pod
NAME                               READY   STATUS             RESTARTS   AGE
ping-deployment-7459f4b7c7-qjpqm   0/1     ImagePullBackOff   0          7m59s

(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl describe pod ping-deployment-7459f4b7c7-qjpqm | less
```
### Loading an image to the cluster

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kind load docker-image ping:v001
Image: "" with ID "sha256:1b7c503bebead7926b8a9dfbcae312495012a7d0afa50e035c06510b4ac467d1" not yet present on node "kind-control-plane", loading...

(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl get pod
NAME                               READY   STATUS    RESTARTS   AGE
ping-deployment-7459f4b7c7-qjpqm   1/1     Running   0          23m
```
Next we need to create a service. But there is a way that we can test the deployment, before creating a service. For that we can do a thing, called **PORT FORWARDING**. 

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl port-forward ping-deployment-7459f4b7c7-qjpqm 9696:9696
Forwarding from 127.0.0.1:9696 -> 9696
Forwarding from [::1]:9696 -> 9696
``` 

Now open another terminal:
```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ curl localhost:9696/ping
PONG
```

## 10.5.4 Creating a service

- peapred `service.yaml file`
- then,
```
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl apply -f service.yaml
service/ping created
``` 
- then,
```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl get service
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP        136m
ping         LoadBalancer   10.96.200.221   <pending>     80:30853/TCP   83s
```

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl get svc
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP        137m
ping         LoadBalancer   10.96.200.221   <pending>     80:30853/TCP   2m11s
```

```
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ kubectl port-forward service/ping 8080:80
Forwarding from 127.0.0.1:8080 -> 9696
Forwarding from [::1]:8080 -> 9696
|
```

in another terminal:
```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving/ping$ curl localhost:8080/ping
PONG
```

In this session, we created a simple PING-PONG application, that when we send a GET request to PING, it replies with PONG, then we deployed with kubernetes, for that we installed kubectl which is a tool for communicating with any kuberntes cluster, then we sinstalled Kind, which is a local kubernetes cluster that we can setup anywhere where we have docker. 

We created a deployment of ping app, then we created a service, used port-forwarding to see if its working locally. 