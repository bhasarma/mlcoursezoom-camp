# 7. Machine Learning in Production: BentoML


## 7.1 Introduction
 
 In this module we'll be talking about open-source model serving library BentoML. BentoML is basically production ready machine learning. 
 
 In module 6, we cleaned a known dataset of people, who applied for credits. We ceated few models to predict whether a customer is likely to default or not and finally we selected a model that performed the best. It was a real life use case, that is seen all the time. Typically this is the type of data that we start with. Then model can be expanded into other types of data as well. 
 
 **Now**, where do we go from here after training our model. We have the trained model available to us. How to get it into the hands of real customers, who are applying for credits. This is the focus of this week's module.
 
 Now a days, it is most likely that if someone is applying for a credit, it is done online. There is also a place e.g. website of the bank where it is taking place. It is likely they are filling out an application form online: let's say it is identical to the data as our model is trained on.
 
 **How** do we connect people who are applying for credits on the websites with our new model? 
 
 In module 5, we pickled our model in a Flask app that can be exposed to in an API endpoint, which serves prediction. This works well in development, but in real world there are lots of other factors to consider e.g. when we are building our service we have to ensure that it is ready for production level traffic. It means that in stead of a few people trying our API, in reality it could be hundreds, thoudands or even more depending on use cases. 
 
 **Goals of this module:**

 - Build, package and deploy a ML service at **scale** using BentoML.

 - learn different ways to customize our service to various use cases

 - make your service **production ready**. 
 
 Whether it is deploying a credit risk model or stable diffusion or whisper model, we have a standard way of deploying our ML models.  
 
 **What it means to be production ready**
 
 - scalability

 - Operational efficicieny: it means being able to maintain your service without having it be your full-time job. You deploy your service to production on day 1. When it breaks or we need to update the code or, the model needs to be updated, what if we need to update the model every week. Making sure we can update it easily.
 
 - repetability i.e. ability to build similar service easily without having to do everything again.
 
 - Flexibility : if we need to react quickly to requirements changes or issues in production
 
 - Resiliency: even if we complete blow up our service, we are easily able to go back to a stable version.
 
 - Easy to use -ity: All great frameworks should be easy to use. 
 
 **What BentoML does**
 
 BentoML makes it easy to create and package  our ML service for production. 
 
 
 **Overview of the module:**
 
 7.2 Building a prediction service
 
 We'll see hands on the fastest way to package our services and deploy it.
 	
 7.3 Deploying our prediction service
 
 7.4 Anatomy of a BentoML service
 
 7.5 Customizing Bentos
 
 7.6 BentoML production deployment
 
 7.7 Custom Runner / framework
 How to create our own ML abstractions if we need to.

 **References**

 1. ML Zoomcamp 7.1 - Intro/Session Overview [youtube link](https://www.youtube.com/watch?v=2viqmJ_NpgE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=67)
  
