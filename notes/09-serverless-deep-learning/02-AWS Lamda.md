## 9.2 AWS Lamda

As discussed in the video 9.1, we'll use AWS Lamda for deplyong our convolutional neural network model trained in module 8. Let's take a look at what AWS Lamda is.

If we type `lamda` in AWS console, we see that `Lambda: Run Code without Thinking about Servers`. This is the main promise of Lambda. All we need to do is, write some function. Then we don't think about creating EC2 instances, creating any servers. So Lambda takes care of everything.

In contrast to module 5, where we used Elastic Beanstalk, under the hood of elastic beanstalk a server is actually created. Here we don't have it. We'll talk about it a bit later.

Let's first see what's inside this Lambda. We see below image:

![Imgur](https://i.imgur.com/xbqSt9J.png) 
figure: screen-shot of AWS Lamda

Now we want to create a new function.

- functions created

We see Lamda function there as below:

```python

import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

```

Above: `event` is the parameter for the Lamda function we have. Whatever we want to pass to the almda function will be passed here. We don't know why `context` is needed. It is usually `None`. 

Let's run a simple "PONG" as below:

```python
import json

def lambda_handler(event, context):
    print("parameters:", event)
    # TODO implement
    return "PONG"
```

Then click on `Test`. Let's call this `event name` as `test` 

The following will be passed to the `event` parameter. 

```
{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
```
It will be passed as a dictionary. We sent a json, then it will be converted from json to dictionary, 

 
We see that, what we all need to do is:

- we just write some code for Lambda function
- we deploy this and
- we can test it

We don't need to create any EC2 machine, EC2 instances. We don't need to think about any servers.

Thus Lambda function is pretty convenient. Good thing about almda is: first of all we don't need to think about the infrastructure for serving your model. Another good thing is we pay per request. We pay only when lamda function is doing something. When its idle and not responding to any request, we are not paying for this. Since we don't need to worry about servers, it's called serverless. 

Delete your function at the ned by going to Actions > Delete function

Each account gets some amount of Lambda requests per month for free.

So it's preetyy convenient. Let's see how we can use it. 

Actually we don't want to use tensor-flow for that, because tensor flow is too big in size. Next lesson we'll see how to use something lighter than tensorflow. In particular we'll take a look at TensorFlow-Lite, which is a lighter versioon of TensorFLow.   