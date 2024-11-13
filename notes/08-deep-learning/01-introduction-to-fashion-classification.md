# 8. Neural Network and Deep Learning

In this session, we'll talk about **neural network** and **deep learning**. Till now, we have dealt with tabular data. Methods that we have used so far like 
linear regression, logistic regression and tree based methods: decision tree, random forest and xgboost can be used to model only tabular data. In this module, 
we will look at a different type of data, namely images. We'll look into the methods to train this type of data. 

## 8.1 Introduction to fashion classification

 In this module, we'll look at images of clothes. The task is to classifiy which type of cloth is an image. It is a **classification** project (a **multi-class classification**). We'll build a model that tells us if an image belongs to one of 10 clothing categories. Use case is e.g. an online classify website. User comes to 
 website and wants to create a listing for clothes. Goal is to make it easier for users.
 
 For this we'll have a service: **fashion classification service**. It'll contain a neural network model. This model will take an image as the input and predict 
 category of the cloth in the image.
 
 Link to the dataset: [full dataset](https://github.com/alexeygrigorev/clothing-dataset)
 
 A subset of the full dataset containing most-populous 10 classes from the full dataset: [small dataset](https://github.com/alexeygrigorev/clothing-dataset-small)
 
 To get the above dataset, go to the link, click on code, then we get the address and then clone it with:


 ```
 (base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK10-11-deep-learning$ git clone https://github.com/alexeygrigorev/clothing-dataset-small.git
 ```
 
 It is worth mentioning here that, in this module we'll put emphasis on practical part and we'll not go into theory behind neural networks. We'll see how to train 
 such models. 
 
 For theory behind go to the following course from Stanford: [https://cs231n.github.io/](https://cs231n.github.io/) 
 
 This course go in detail for neural networks in particular for convolutional neural networks for visual recognition. Notes here are quite good. There are also videos.

 ***keywords:**
 Neural Network, Deep Learning and Image Classification.
 