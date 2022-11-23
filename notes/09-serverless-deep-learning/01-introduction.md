# 9. Serverless Deep Learning

In this module, we'll deploy the clothes classification model we trained previously. 

## 9.1 Introduction to serverless

In this week's module, we'll talk about serverless deep learning. Last week, we talked about deep learning and we trained a model for classifying images of clothes. 

Our use case was that an user comes to an online platform wants to sell some clothes in the platform. He uploads some images of clothes that he wants to sell. Idea is to train a model that can predict whether the cloth is a t-shirt or a cap etc. 

For this, once the picture is uploaded by the user, picture will be sent to clothes classification service and the service replies that this is a t-shirt r pant. Then we tell the user, looks like you are trying to sell a t-shirt. So let's put whatever you are trying to sell in the t-shirts category. 

In the previous session, we trained a model. In this session we'll talk about how to take this model and how to deploy this service. 

One way of deploying this is by using  **AWS Lamda**. Lamda is a service from AWS that allows us to deploy many different things including machine learning models. 

The way it works is: we have a picture of pants, we send this picture (url of this picture) to our model that we are going to deploy with AWS lamda, then the service we deploy with lamda will reply with many classes and one this class would be pants, then we'll have some scoresand then we'll respond to the user that you are seliing  a pant.

This is what we are going to cover in this session. 

We'll start with the model that we trained previously with keras. We'll use **tensorflow lite** internally for that. We'll talk about why tensoeflow-lite is better than plain tensorflow for this particular use case. That's the plan for this session.    