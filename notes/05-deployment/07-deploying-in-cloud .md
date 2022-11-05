# Deploying Docker Container to the Cloud : AWS Elastic Beanstalk

We need to install a special CLI for elastic beanstalk. its called `awsebcli`. We will not install it here, we mean in miniconda or in anaconda. We'll not install it systemwide. We want to install it only for this project. For this we'll use `pipenv`, the virtual environment that we are using in this week's module. 

We'll do it by:
`$ pipenv install awsebcli --dev`

We'll use it only when we are deploying or developing. Thus it is a dev-dependency. We don't need to have it inside the container. This is specified with `--dev`. Now we can use this `awsebcli`.

Now just doing `awsebcli` on terminal is not recognized. Thus we need to do first: 

   `$ pipenv shell`
   
   Then inside the shell `eb` command is found.
   
   Now we'll use this command line tool to use our service into elastic beanstalk. for that we use:
   
   `$ eb init -p docker -r eu-west-1 churn-serving`
   
## Testing if the server works locally

`$ eb local run --port 9696`

Test it by going to another terminal and using the script `python predict-test.py`. 


## Run web service on the cloud 

`eb create churn-serving-env`

This will create an elastic beanstalk env, that is called churn-serving-env.
We'll some things going on in the terminal. It will create a load balnacer for us e.g. It creates a production ready environment, that is able to scale up and down, when we need. 

Then we that: `Application available at .....address`. We copy this addres. Paste this into `predict-test.py` as shown in video 12:00 minutes of 5.7. 

**Warning:**
With these default settings, that we used now for elastic beanstalk, it created a service that is open to the world. Right now, if somebody gets this address, they can also starts using it, they can also send request. Of course we'll disable this. I will turn it down after I finish recording this. We need to be careful with that. Maybe we just open it for your computer or maybe for the services e.g. in our case marketing service. We can find a lots of material online how to do this or ask some of your friends who are cloud specialist, who can help you to do this if you don't know how to do this. But for pet project, like this one, don't forget to take it down. 


We will terminate it. But before we terminate it let's see how it looks from console. We can terminate from there as well. 

![Imgur](https://i.imgur.com/8h35pjL.png)

Or, we can terminate from our terminal inside the virtual environment: 
`$ eb terminate churn-serving-env`  