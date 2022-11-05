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


**Business Problem Description**

Banks are the most influential financial institutions of our time. They make revenue by selling their products to their customers. Some examples of products of a bank are savings account, credit card, personal loan, house loan etc. In this project, a bank wants to launch a campaign to sell a product called `term-deposit`. This particular bank wants to do a targeted campaign, i.e. they want to call, send an email or post to targeted customers out of lots of customers. Fortunately, we have datas from a previous campaign. This dataset contains demographic and banking information about the customers, that were part of previous campaign and also the outcome of the campaign, i.e. whether they acecepted the product after the campaign or not. In this project, we want to train a model on this dataset in order to predict whether a targeted campaign on a particular customer will be successful or not. This is binary classification problem

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
## Conclusions

- 4 models (logistic regression, decision tree, random forest and XGboost)  were trained on the dataset
- Best model is: xx with accuracy of xx

## References

- [Github repository of the course Machine Learning Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) 
- [Youtube Playlist where course videos are hosted](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) 
- [Photo by Monstera from Pexels](https://www.pexels.com/photo/cutout-paper-composition-of-bank-with-dollar-bills-5849548/)

## Contacts
Any feedback, question or suggestion? Feel free to contact me!<br>
[<img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:b.sarma1729@gmail.com)


If you like the work, consider clicking on the ⭐.