# Subscription to Bank Term Deposit Prediction

*"No great marketingdecisions have ever been made on qualitative data" - John Scully (CEO of Apple Inc. 1983-1993)*

![Imgur](https://i.imgur.com/qGlDEkY.jpg)
Photo Credit: Photo by Monstera from Pexels

This repository contains the project carried out during the midterm project of online course Machine Learning Zoomcamp designed and instructed by [Alexey Grigorev](https://github.com/alexeygrigorev) and his team from [DataTalks.Club](https://datatalks.club/). This project is 2 weeks long and peer-reviwed.

## Table of Contents:

1. Problem Description
2. About the Dataset 


**Problem Description**

Banks are the most influential financial institutions of our time. They make revenue by selling their products to their customers. Some examples of products of a bank are savings account, credit card, personal loan, house loan etc. In this project, a bank wants to launch a campaign to sell a product called `term-deposit`. This particular bank wants to do a targeted campaign, i.e. they want to call, send an email or post to targeted customers out of lots of customers. Fortunately, we have datas from a previous campaign. This dataset contains demographic and banking information about the customers, that were part of previous campaign and also the outcome of the campaign, i.e. whether they acecepted the product after the campaign or not. In this project, we want to train a model on this dataset in order to predict whether a targeted campaign on a particular customer will be successful or not. This is binary classification problem

**About the dataset**

The dataset has 18 features and 45211 rows. Below are the detailed information about the features:


|  Feature Name  |             Description             |
|:--------:|:-----------------------------------:|
|    **Id**   |  customer identification number  |
|    **age**   |  age of the customer |
|    **job**   |  job of the customer |
|   **marital**   | marital status of the customer |
| **education** |    education qualification of the customer   |
| **default** |  whether customer has credit in default  (binary: "yes", "no")  |
|  **balance**  |  average yearly balance of the customer in Euros  |
| **housing**  |  whether customer has housing loan (binary: "yes", "no")  |
| **loan**  |  whether customer has personal loans (binary: "yes", "no")  |
| **contact**  |  bank's contact communication type with the customer  (categorical : "telephone", "cellular", "unknown")  |
| **day**  |  last contact day of the month (numeric)  |
| **month**  |  last contact month of year (categorical: "Jan", "feb", "mar", ...."nov","dec" |
| **duration**  |  last contact duration in seconds (numeric)  |
| **campaign**  |  number of contacts performed during this campaign and for this customer (numeric)  |
| **pdays**  |  number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means that client was not previously contacted  |
| **previous**  |  number of contacts performed before this campaign and for this customer (numeric)  |
| **poutcome**  |  outcome of previous marketing campaign (categorical: "unknown", "other", "failure", "success"  |
| **y**  |  target variable, has the client subscribed to a term deposit product? (binary: "yes","no") |


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
