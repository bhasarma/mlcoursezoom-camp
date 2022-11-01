# 5. Deploying Machine Learning Models


## 5.1 Overview

Till week 04, we have trained churn prediction model and we evaluated it. Now we take our trained and evaluated model and deploy it as a **web service**. This means, we want to take the model, save it and use it. How we want to use it is sketched in figure 1.

We have first of all our jupyter notebook. We train and evaluate the model in it. Then we save it to a file `model.bin`. We want to load this file from a different process called **web-service**. Let's call it churn-service for our case. churn-service has the model in it. 

Now let's imagine another service called **marketing-service**. It contains information about all the customers. Their id, age, services used etc. Marketing-service want to know whether a person is likely to churn or not. Then it can decide on which customer to send a promotional email.

The way it works is **marketing-service** will send a **request** to churn-service with the data about a particular cusomer. Then, **churn-service** witll apply model to this customer's data and will send the prediciton to the **marketin-service**. In this module of week-05, we'll see the part separated with thick yellow line. 

We'll see how to interact with this service. This is focus of this module.

![Imgur](https://i.imgur.com/K8Alpyc.png)
 
Figure 1: sketch of overview of model deployment


![Imgur](https://i.imgur.com/t1iUVUW.png)

Figure 2: sketch of different layers in model deployment 

To be able to intereact with the **web-service**, we start with our model. We have our churn-prediction model. 

* We put our model inside a web-service. We'll use **Flask** for that. This is a framework for creating services in python.
* Then we want to isolate the dependencies for this service in such a way that, they don't interfere with other services that we have in our machine. For this we want to create a special environment for python dependencies. We use `pipenv` for that. 

* Then we add another layer on top. This layer is a lyer with system dependencies. We use **docker** for that. 

*  Finally after all thse layers, we'll deploy this in a cloud. We'll take the container and deploy to a ***AWS Elastic Beanstalk***. 

## 5.2 Saving and Loading the Model
Here we'll talk about:

* Saving the model to pickle
* Loading the model from pickle
* Turning our notebook into a python script

## 5.3 WebServices: Introduction to Flask
Here we'll talk about web-services and we'll talk about a framework, a python framework for creating web-services called Flask.

As discussed in figure 1, in order to use our model, we want to put our model inside churn-service and marketing-service will communicate with our churn-service. It will send some request and it'll get some response. Instead of running the `predict.py` script having customer details inside the script, we want to run it as a web-service.

**What is web service?**
If we just google it, we see that it is a method (or, service) for communication between two electronics devices over a network using some protocol.  

As shown in figure 3, let's say we have a web-service and we have a user for our web-service. An user is somebody who wants to make a request with some information with the request.  E.g. if I do a gogle search with the word apple, then I make a request to a web-service with some parameter `q=apple`. Then I get back result, whatever this web-service wants to do with this query. In this particular example of google query, google web-service returns us results with list of web-pages. Web services communicate over some protocols. We don't need to worry about it. We can use `Flask` for implementing that. It takes care of all the internals. All we need to know is how we can communicate with this. 

![Imgur](https://i.imgur.com/4EXkJah.png)
Figure 3. sketch of web-services.

Let's create a simple service as shown in figre 4. We want to create a service that the user send a query to `ping` address and gets replies with `pong`. Let's create now a web-service usigng Flask.  

![Imgur](https://i.imgur.com/tryFw53.png)
Figure 4: sketch of a simple ping-pong query

* writing a simple ping/pong app

![Imgur](https://i.imgur.com/RdUjPo4.png)

* Querying it with `curl` and browser

### References
1. Machine Learning Zoomcamp Material
[https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/05-deployment](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/05-deployment)