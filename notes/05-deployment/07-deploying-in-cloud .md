# Deploying Docker Container to the Cloud : AWS Elastic Beanstalk

In this lesson we'll talk about deploying our docker container to the cloud.
In the previous lesson we built a docker image or, a docker container. We built our churn-prediction service there. We put the model there. We built this image and we learnt how to run it localy. Now we want to take this image and deploy it to the cloud. 

For this particular lesson, we choose AWS. It is probably the most popular cloud provider. Elastic Beanstalk is relatively simple. There are just a few commands we need to run to be able to deploy something to the cloud. We can explore other options like Heroku, Google Cloud, Azure or pythonAnywhere or other cloud providers. 

If you don't have an account in AWS, then create an account following the instruction in this article: [creating an aws account](https://mlbookcamp.com/article/aws). This asks for a credit card information from the user, although we are going to work in the free tier range. 

It is assumed for now that, you can access your aws account programmaticalls using CLI or something. 

 We need to install a special CLI for elastic beanstalk. its called `awsebcli`. We will not install it here, we mean in miniconda or in anaconda. We'll not install it systemwide. We want to install it only for this project. For this we'll use `pipenv`, the virtual environment that we are using in this week's module. 

We'll do it by:
`$ pipenv install awsebcli --dev`

We'll use it only when we are deploying or developing. Thus it is a dev-dependency. We don't need to have it inside the container. This is specified with `--dev`. Now we can use this `awsebcli`.

Now just doing `awsebcli` on terminal is not recognized. Thus we need to do first: 

   `$ pipenv shell`
   
   Then inside the shell we ca do `eb` and we see that command is found.
   
   Now we'll use this command line tool to use our service into elastic beanstalk. for that we use:
   
   `$ eb init -p docker -r eu-west-1 subscription-serving`
   
   I had to give my aws-acccess-id and aws-secret-key.
   
   Then it sais 'Application subscription-serving has been created.' 
   
## Testing if the server works locally
With ls -a we see that folder .elasticbeanstalk is created. 

`$ eb local run --port 9696`

Test it by going to another terminal and using the script `python predict-test.py`. 

## Run web service on the cloud 

`eb create churn-serving-env`

This will create an elastic beanstalk env, that is called churn-serving-env.
We'll some things going on in the terminal. It will create a load balnacer for us e.g. It creates a production ready environment, that is able to scale up and down, when we need. 

Then we that: `Application available at .....address`. We copy this addres. Paste this into `predict-test.py` as shown in video 12:00 minutes of 5.7. 

Then we run `python predict-test.py` on our terminal and we get our result.

**Warning:**
With these default settings, that we used now for elastic beanstalk, it created a service that is open to the world. Right now, if somebody gets this address, they can also starts using it, they can also send request. Of course we'll disable this. I will turn it down after I finish recording this. We need to be careful with that. Maybe we just open it for your computer or maybe for the services e.g. in our case marketing service. We can find a lots of material online how to do this or ask some of your friends who are cloud specialist, who can help you to do this if you don't know how to do this. But for pet project, like this one, don't forget to take it down. 


We will terminate it. But before we terminate it let's see how it looks from console. We can terminate from there as well. 

![Imgur](https://i.imgur.com/8h35pjL.png)

Or, we can terminate from our terminal inside the virtual environment: 
`$ eb terminate churn-serving-env`  