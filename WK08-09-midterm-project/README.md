# Subscription to Bank Term Deposit Prediction

*"No great marketing decisions have ever been made on qualitative data" - John Scully (CEO of Apple Inc. 1983-1993)*

![Imgur](https://i.imgur.com/qGlDEkY.jpg)
Photo Credit: Photo by Monstera from Pexels

This repository contains the project carried out during the midterm project of online course Machine Learning Zoomcamp designed and instructed by [Alexey Grigorev](https://github.com/alexeygrigorev) and his team from [DataTalks.Club](https://datatalks.club/). This project is 2 weeks long and peer-reviewed.

## Table of Contents:

1. Business Problem Description
2. About the Dataset
3. Project Workflow
4. Steps to run the application 


**1. Business Problem Description**

Banks are the most influential financial institutions of our time. They make revenue by selling their products to the customers. Some examples of products from a bank are savings account, credit card, personal loan, house loan etc. A bank (name unknown) wants to launch a campaign to sell a product called `term-deposit`. This particular bank wants to do a targeted campaign, i.e. they want to call, send an email or post to targeted customers, who are likely to buy this product. The goal of this project is to predict whether a customer is likely to buy this product or not.  Fortunately, this bank has datas from a previous campaign. This dataset contains demographic and banking information about customers and also the outcome of the campaign, i.e. whether they subscribed to the product after the campaign or not. In this project, we want to train a model on this dataset in order to predict whether after a targeted campaign, a particular customer will subscribed to the product 'term deposit' or not. Since we want our model to predict yes or no, this is a binary classification problem.

**About the dataset**

The dataset has 18 features and 45211 rows. In the table below, meaning of each feature is written


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

*In the table above almost all features are self explanatory, except `day` and `month`.  Both the features together mean, last contact date e.g. a `day = 2`, and `month = may` would mean, customer was contacted last on 2nd May. We don't know the year, but it is not relevant for our training. 

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



**Deploying our docker container to the cloud with AWS EB**

## Conclusions

- 4 models (logistic regression, decision tree, random forest and XGboost)  were trained on the dataset
- Best model is: xx with accuracy of xx

## References

- [Github repository of the course Machine Learning Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) 
- [Youtube Playlist where course videos are hosted](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) 
- [Photo by Monstera from Pexels](https://www.pexels.com/photo/cutout-paper-composition-of-bank-with-dollar-bills-5849548/)

## Contacts
Any feedback, question or suggestion? You are welcomed to contact me!<br>


[<img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:b.sarma1729@gmail.com)


Last but not the least, if you like the work, consider clicking on the ⭐