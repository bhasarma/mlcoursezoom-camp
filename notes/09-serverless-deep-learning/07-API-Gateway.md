## 9.7 API Gateway: Exposing the lambda function

In this session, we'll take the lamda function we created in the previous session and we'll expose it as a webservice. To achieve this, we'll use **API Gateway**. This is a service from AWS that let's us expose different AWS services as webservices including Lambda function. 

1 Go to API Gateway on AWS. 

Conclusion:
- this is ow we turned our lambda function into a webservice. 

**Alert:**
***Creating and configuring the Gateway:***

Right now this lambda function is open. I have access to the url from API Gateway. I will be able to send something to this url as well. We don't want to open it at work. This is not ideal. Your service is to everyone in the world. You need to be little bit careful with how you do this. This is outside of the scope of this course. But this is something to keep in mind. For learning its fine. Please don't do this at work and talk to people who know AWS and who can help you configure in such a way that its limited only to those who need to invoke this function. 

   
