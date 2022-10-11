# 6. Decision Trees and Ensemble Learning

In this module we'll talk about decision trees and ensemble learning. 

We'll do this through the project Credit Risk Scoring.

## 6.1 Credit Risk Scoring project

Let's imagine you (a customer) want to buy a mobile phone. You go to a bank and ask for a loan from the bank to buy this phone. You fill in a application form that asks for some details such as your income, how much the phone cost, how much money you want from the bank, do you own a house etc. You fill in the application form. send it to the bank and ask for money. Bank looks at the information that you have put in the form and say yes or no based on this information. Bank is taking its decision by analyzing the information about you. 

In this module, we want to build a **model** that the bank can use to make the decision, if they should lend you the money or not. Bank will give to the model information about you as input and model will respond with what is th risk that this customer will or will not pay back. A customer not paying back is called **default**. The model is going to return the probability or risk that the customer is going to default i.e. **risk of defaulting**. Based on risk of defaulting, bank will decide, whether to lend money to you or not.

![Imgur](https://i.imgur.com/bmfbATu.png)
**Figure 1**: sketch depicting customer giving information to bank and bank deciding yes or no based on risk of defaulting. 

A bank can make a decision based on a customer's information by analyzing informations about all the customers that it already has.  Bank has all the applications from all the customers, all the informations about them, how much money they asked for and which customer was a default and which wasn't. 

![Imgur](https://i.imgur.com/txc1Jab.png)
**Figure 2**: sketch of feature matrix $X$ and target variable $y$. $X$ contains informations about customers and $y$ is $0$ or $1$.  $g(X_{i})$ is the model.


We want to train a model from the informations / data about the existing customers. For each new customer this model will give us a probabilty of default or no default.  Model $g(X_{i})$ as defined early will give us the probability of default. X is the feature matrix with all the information about the existing customers that the bank has. $y$ is our target variable. Values of y is either $0$ or $1$. $1$ means DEFAULT and $0$ means NO DEFAULT.  Thus it is a binary classification problem.

In the next lessons this week, we'll talk about this dataset, apply few other algorithms into it and will finally select the best model.



**References**
1. ML Zoomcamp 6.1 - Credit Risk Scoring Project [lesson on youtube](https://www.youtube.com/watch?v=GJGmlfZoCoU&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=57&t=1s)
2. ML Zoomcamp 6.1 [slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-6-decision-trees-and-ensemble-learning)