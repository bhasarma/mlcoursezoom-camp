# Subscription to Bank Term Deposit Prediction

*"No great marketing decisions have ever been made on qualitative data" - John Scully (CEO of Apple Inc. 1983-1993)*

![Imgur](https://i.imgur.com/qGlDEkY.jpg)
Photo Credit: Photo by Monstera from Pexels

This repository contains the project carried out during the midterm project of online course Machine Learning Zoomcamp designed and instructed by [Alexey Grigorev](https://github.com/alexeygrigorev) and his team from [DataTalks.Club](https://datatalks.club/). This project is 2 weeks long and peer-reviewed.

## Table of Contents:

1. Business Problem Description
2. About the Dataset
3. About files and folders in this repo
4. Project Workflow 
5. Conclusions
6. Contact


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


## Project workflow

- Development system: 
   OS: Ubuntu 18.04.6 LTS
   Architecture: x86_64
   conda virtual env 

There are different ways to interect with this project:
   
- If you want to play with `notebook.ipynb` file where all analysis of the dataset from importing data, exploraray data analysis to training different models are done, you can do it localy using the jupyter notebook. You need to install conda env and have jupyter notebook installed.

- If you want to do test for one cutomer, you can do it on `notebook_without_output_test.ipynb` file. You can play here by changing variables of the customer and get a probabibility score. This is also the notebook, that is finally converted into a python script `train.py`

- You can locally run  `train.py` and save the model with the command `python train.py`. An example of my CLI is below:

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK08-09-midterm-project$ conda activate ml-zoomcamp
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK08-09-midterm-project$ ls
customer.py  notebook.ipynb                      predict.py                     README.md
model.bin    notebook_without_output_test.ipynb  predict-term-deposit-data.csv  train.py
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK08-09-midterm-project$ python train.py 
/home/bsarma/anaconda3/envs/ml-zoomcamp/lib/python3.9/site-packages/sklearn/utils/deprecation.py:87: FutureWarning: Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
  warnings.warn(msg, category=FutureWarning)
training the xgboost model with eta=0.1, max_depth=6 and min_child_weight=10
Result of Final Gradient Boosting Model:
ROC AUC score: 0.941
the model is saved to model.bin
```
- you can also run `predict_v1.py`, a file that loads the saved model and gives a probability as output. Its implementation is shown below:

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK08-09-midterm-project$ conda activate ml-zoomcamp
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK08-09-midterm-project$ ls
customer.py  notebook.ipynb                      predict.py                     predict_v1.py  train.py
model.bin    notebook_without_output_test.ipynb  predict-term-deposit-data.csv  README.md
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK08-09-midterm-project$ python predict_v1.py 
/home/bsarma/anaconda3/envs/ml-zoomcamp/lib/python3.9/site-packages/sklearn/utils/deprecation.py:87: FutureWarning: Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
  warnings.warn(msg, category=FutureWarning)
input: {'age': 25.0, 'job': 'blue-collar', 'marital': 'married', 'education': 'secondary', 'default': 'no', 'balance': 11674.0, 'housing': 'yes', 'loan': 'no', 'contact': 'unknown', 'day': 5, 'month': 'may', 'duration': 257, 'campaign': 1, 'pdays': -1, 'previous': 0, 'poutcome': 'yes'}
```
#### Webservices
We create a webservice (called `subscription service`) using python framework Flask. This is basically where we turn `predict.py` into a webservice called `subscription`. 

1. This webservice can be run on from Jupyter Notebook (done in 5.4 video). We see that there is a warning ` WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead`.

Therefore, inseatd of using plain flask we need to use WSGI server. There are many different WSGI servers available in python. We use gunicorn. Install it with `pip install gunicorn`.

Then run the app with the following commands:
`$ gunicorn --bind 0.0.0.0:9696 predict:app`
and open a jupyter notebook `predict-test.ipynb` to test predict app.
This way we turned our Flask app into production-ready. This we'll use now for deplying our services.

- `predict-test.py` is downloaded script from `predict-test.ipynb`
Now we can in one terminal run `python predict.py` and in another terminal `python predict-test.py`. 


**Python virtual env: pipenv**
Subscription web service is put inside a python virtual environment  `pipenv`. 
1. `pip install pipenv`

2. `pipenv install numpy scikit-learn==0.24.2 flask gunicorn`

Now if we want to run our webservice: 
1. activate this project's virtualenv, by runnin `pipenv shell`
2. Then run `gunicorn --bind 0.0.0.0:9696 predict:app`

In stead of running above two commands, you can also just write `pipenv run gunicorn --bind 0.0.0.0:9696 predict:app`. It does the same. 

======
Clone this repo and after cloning just do `pipenv install`. You are good to go.
 
### Environment Management with Docker
- build docker file with `docker build -t midterm-project .`
- run the service with `docker run -it --rm -p 9696:9696 midterm-project:latest`
- make a request with `python predict-test.py` in another terminal, of course in the same dir where the file is.



### Deploying the docker container to the cloud with AWS EB
As the final step, we deploy our docker container built in the previous step to the cloud. We use AWS Elastic Beanstalk for this work.

- if you don't have an account yet in AWS, you can create one by following the instructions in the article [creating an aws account](https://mlbookcamp.com/article/aws). In order to create an account, it asks for credit card information. However we are going to use only the free tier resources for this project.

- create an EC2 instance on AWS following the instructions [here](https://mlbookcamp.com/article/aws-ec2).

- Then install the special CLI for elastic beanstalk `awsebcli` in the pipenv of this project with the following commands in your terminal and in the directory where this project is. In my case it is `(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK08-09-midterm-project$`.

command 1: `$ pipenv install awsebcli --dev`

command 2: Enter the pipenv environement with: 
`$ pipenv shell`

Use the service with the following command: 
`$ eb init -p docker -r eu-west-1 subscription-serving` 

If it is your first time, then it will ask for your `aws-acccess-id` and `aws-secret-key`. Enter them and wait till it says `Application subscription-serving has been created.`

### Testing if the server works locally
We can first test, if the server works localy with the command:
`$ eb local run --port 9696`.
Test it by going to another terminal and running the script `python predict-test.py`

### Running the web service in the cloud
Create an elastic beanstalk env by:
`eb create churn-serving-env`

It takes some time we'll see `Application available at .....address`. We copy this addres. Paste this into predict-test.py 

- run `python predict-test.py` on our terminal and we get our result in the terminal.

**Important:**  For security reasons, we are not running the service anymore. We have taken it down. Below you can see a video-scrennshot of the service running.

[Video link here](https://www.veed.io/view/ae183e54-8ab0-410b-8f22-86d60630d26c?panel=share)

- terminate the service at the end by: `eb terminate subscription-serving-env`

## Conclusions

- 4 models (logistic regression, decision tree, random forest and XGboost)  were trained on the dataset
- Best model is: xx with accuracy of xx

## References

- [Github repository of the course Machine Learning Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) 
- [Youtube Playlist where course videos are hosted](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) 
- [Photo by Monstera from Pexels](https://www.pexels.com/photo/cutout-paper-composition-of-bank-with-dollar-bills-5849548/)

## Contacts
If you face problem in running any part of the project, contact me at `b.sarma1729[AT]gmail.com` or dm on slack channel `@Bhaskar Sarma`.

Last but not the least, if you like the work, consider clicking on the ⭐