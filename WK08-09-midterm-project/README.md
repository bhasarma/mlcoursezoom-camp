# Subscription to Bank Term Deposit Prediction

*"No great marketing decisions have ever been made on qualitative data" - John Scully (CEO of Apple Inc. 1983-1993)*

![Imgur](https://i.imgur.com/qGlDEkY.jpg)
Photo Credit: Photo by Monstera from Pexels

This repository contains the project carried out during the midterm project of online course Machine Learning Zoomcamp designed and instructed by [Alexey Grigorev](https://github.com/alexeygrigorev) and his team from [DataTalks.Club](https://datatalks.club/). This project is 2 weeks long and peer-reviewed.

## Table of Contents:

1. Business Problem Description
2. About the Dataset
3. About files and folders in this repo
4. Development System
5. How to reproduce the project
6. Conclusions
7. References


## 1. Business Problem Description

Banks are the most influential financial institutions of our time. They make revenue by selling their products to the customers. Some examples of products from a bank are savings account, credit card, personal loan, house loan etc. A bank (name unknown) wants to launch a campaign to sell a product called `term-deposit`. This particular bank wants to do a targeted campaign, i.e. they want to call, send an email or post to targeted customers, who are likely to buy this product. The goal of this project is to predict whether a customer is likely to buy this product or not.  Fortunately, this bank has datas from a previous campaign. This dataset contains demographic and banking information about customers and also the outcome of the campaign, i.e. whether they subscribed to the product after the campaign or not. In this project, we want to train a model on this dataset in order to predict whether after a targeted campaign, a particular customer will subscribed to the product 'term deposit' or not. Since we want our model to predict yes or no, this is a binary classification problem.

## 2. About the dataset

The dataset has 18 features and 45211 rows.


- You can get the dataset from [kaggle](https://www.kaggle.com/datasets/aslanahmedov/predict-term-deposit)

 - or, from this wget-able [link](https://raw.githubusercontent.com/bhasarma/mlcoursezoom-camp/main/WK08-09-midterm-project/predict-term-deposit-data.csv):
 
 ```
 wget https://raw.githubusercontent.com/bhasarma/mlcoursezoom-camp/main/WK08-09-midterm-project/predict-term-deposit-data.csv
 ```
 
 In case, your are running this `bash` command inside a Jupyter Notebook instead of a termical, don't forget to put a `!` before `wget`. No space needed between `!` and `wget`

In the table below, meaning of each feature is written.


|  Feature Name  |             Description             |  Datatype  |
|:--------:|:-----------------------------------:|:-----------------------------------:|
|    **Id**   |  customer identification number  |   int    |
|    **age**   |  age of the customer |    float  | 
|    **job**   |  job of the customer |    string  |
|   **marital**   | marital status of the customer | string |
| **education** |    education qualification of the customer   | string |
| **default** |  whether customer has credit in default | binary:yes or no| 
|  **balance**  |average yearly balance of the customer in Euros  |float | 
| **housing**  |  whether customer has housing loan| binary: yes, no |
| **loan**  |  whether customer has personal loans | binary: yes, no |
| **contact**  |  bank's communication type to contact the customer | string: telephone, cellular and unknown |
| **day***  |  last contact day of the month | int |
| **month***  |  last contact month of year|  string: jan, feb, mar, ....,nov and dec |
| **duration**  |  last contact duration in seconds| int |
| **campaign**  |  number of contacts performed during this campaign with the customer  | int | 
| **pdays**  |  number of days that passed by after the client was last contacted from a previous campaign (-1 means that client was not previously contacted  | int  |
| **previous**  |  number of contacts performed before this campaign with the customer | int | 
| **poutcome**  |  outcome of previous marketing campaign | string: unknown, other, failure and success  |
| **y**  |  target variable, has the client subscribed to a term deposit product? | binary: yes or no |

*`day` and `month`, both the features together mean, last contact date e.g. a `day = 2`, and `month = may` would mean, customer was contacted last on 2nd May. We don't know the year, but it is not relevant for our training. 

## 3. About files and folders in this repo

|  File name |      Description       |
|:--------:|:-----------------------------------:|
|    **README.md**   |  The file you are reading now, meant for the user containing details about the project| 
|    **predict-term-deposit-data.csv**   |  Dataset file explained in the previous section |
|    **notebook.ipynb**   |  Jupyter notebook file where all EDA, training different models, hyperparameterization etc. are carried out in development |
|    **train.py**   |  python script that is converted from `notebook.ipynb` with only core logic and best model in it |
|    **model.bin**   |  saved model which is obtained as output of `train.py` |
|    **environment.yml**   |  dependency yaml file exported from the conda environement used for develpment |
|    **predict.py**   |  python script that loads the model and puts in a Flask webservice app called `subscription`|
|    **Pipfile**   |  python virtual environment management (pipenv) file with all the used packages and their versions listed (used for deployment)|
|    **Pipfile.lock**   |  python virtual environment management(pipenv) file specifying which specific version of the packages present in `Pipfile` should be used (used for deployment)|
|    **Dockerfile**   |  Dockerfile that is built to create docker container image|
|    **predict-test.py**   |  python script that sends a request to the host in aws cloud with the customer information and returns subscription probability and whether the customer will subscribe to the term deposit|
|    **dev_files**   |  A folder containing files used during development, but no longer relevant for deployment. Helpful to run locally to understand the project |


## 4. Development System
  
   OS: Ubuntu 18.04.6 LTS
   
   Architecture: x86_64
   
  conda virtual environment for development
  
  pipenv for deployment

## 5. How to reproduce the project

In order to reproduce this project, first of all, clone this repo in your local machine with the command:

```
git clone  https://github.com/bhasarma/mlcoursezoom-camp/tree/main/WK08-09-midterm-project.git
```
Now go inside the project directory with the command:
```
cd WK08-09-midterm-project
```
## Development part of this project


Development part i.e. till training the models in Jupyter notebook, finding the best model and saving it, is done in a conda environment. If you want to run the notebook localy, then you have to recreate the conda environment that I used for development. For this, you first have to install Anaconda on your system, if you have not done it already. Install it by following these instructions in this [Anaconda](https://www.anaconda.com/products/distribution) page. This Site automatically detects the operating system and suggest the correct package.

I have created a `environment.yml` dependency file by running the command `conda env export > environment.yml` inside my activated conda envirnment. You can now recreate this environment with the command:

```
conda env create -f environment.yml
``` 
You can check if the environment `ml-zoomcamp` is created by listing all the conda environment available with the command:

```
conda info --envs
```
Activate the environment with:

```
conda activate ml-zoomcamp
```

Now you should be able to run `train.py` and save the model localy with:

```
python train.py
```
You can also go to jupyter notebook `notebook.ipynb`, run it and play with it.

## Deployment part of this project

Saved model is loaded and put inside a webservice called `subscription` using Flask (see `predict.py`). This service is then put inside a python virtual environment `pipenv`. In order to recreate this environment `Pipfile` and `Pipfile.lock` is provided. 

If you haven't installed `pipenv` yet, you need to do it with:
```
pip install pipenv
```
Then you can recreate the environment by running the below command in the project directory:
```
pipenv install
```
### Environment Management with Docker
Subscription-service app is then put inside a docker container (see `Dockerfile`). Before we can run a docker image, first it has to be built with the command:

```
docker build -t midterm-project
```

Then, run the service with 
```
docker run -it --rm -p 9696:9696 midterm-project:latest
```
Make a request by running below command in another terminal.

```
python predict-test.py
``` 

After Docker container is built, it can be deployed to the cloud. 

### Deploying the docker container to the cloud with AWS Elastic Beanstalk

As the final step, we deploy our docker container built in the previous step to the cloud. 

- if you don't have an account in AWS, you can create one by following the instructions in the article [creating an aws account](https://mlbookcamp.com/article/aws). In order to create an account, it asks for credit card information although, we are going to use only the free tier resources for this project.

- create an EC2 instance on AWS following the instructions [here](https://mlbookcamp.com/article/aws-ec2).

- Install the special CLI for elastic beanstalk `awsebcli` inside the pipenv of this project with the following commands in your terminal and in the project directory. In my case e.g. it is `(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK08-09-midterm-project$`.

```
pipenv install awsebcli --dev
```

- Then enter the pipenv environement with: 
```
pipenv shell
```

- Use the service with the following command: 
`$ eb init -p docker -r us-east-1 subscription-serving` 

Use your preferred region. I have used `us-east-1`.

If it is your first time, then it will ask for your `aws-acccess-id` and `aws-secret-key`. Enter them and wait till it says `Application subscription-serving has been created.`

### Testing if the server works locally
- We can first test, if the server works localy with the command:
`$ eb local run --port 9696`.

- Test it by going to another terminal and running the script `python predict-test.py`

### Running the web service in the cloud

- Create an elastic beanstalk env by:

```
eb create subscription-serving-env
```

It takes some time. We'll see `Application available at .....address` on the terminal. Copy this addres and paste into `url` variable in `predict-test.py`. 

- Run `python predict-test.py` on your terminal and get the prediction result in the terminal.

![Imgur](https://i.imgur.com/1BcKlad.png)
Figure: Screenshot of prediction about a customer ran on host address url `http://subscription-serving-env.eba-meke3qbg.us-east-1.elasticbeanstalk.com/predict`.

**Important:**  For security reasons, subscription-service in the cloud is stopped. It has been taken down. Below you can see a video me interacting with the running service.

[Video link here](https://www.veed.io/view/ae183e54-8ab0-410b-8f22-86d60630d26c?panel=share)

Also a screenshot of the service running in the cloud can be seen below:

![Imgur](https://i.imgur.com/8OBzN08.png)

- Finally, don't forget to terminate the service at the end by: `eb terminate subscription-serving-env`

## 6. Conclusions

- 4 models: logistic regression, decision tree, random forest and XGboost were trained on the dataset
- parameter tuning was done for each model
- XGboost model is found to be the best performing model with an ROC AUC score of 0.941
- Best model was saved, loaded into a webservice using Flask and deployed to the AWS cloud. 

## 7. References

- [Github repository of the course Machine Learning Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) 
- [Youtube Playlist where course videos are hosted](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) 
- [Photo by Monstera from Pexels](https://www.pexels.com/photo/cutout-paper-composition-of-bank-with-dollar-bills-5849548/)

## Contacts
If you face any problem in running any part of the project: 

- contact me at `b.sarma1729[AT]gmail.com` or,

- dm on DataTalks.Club slack `@Bhaskar Sarma`.

Last but not the least, if you like the work, consider clicking on the ⭐