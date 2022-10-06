# 5.1 Deploying Machine Learning Models

Till week 04, we have trained churn prediction model and we evaluated it. Now we take our trained and evaluated model and deploy it as a web service. This means, we want to take the model, save it and use it. How we want to use it is sketched in figure 1.

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

### References
1. Machine Learning Zoomcamp Material
[https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/05-deployment](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/05-deployment)