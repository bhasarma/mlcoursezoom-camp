# 6. Decision Trees and Ensemble Learning

In this session we'll talk about decision trees and ensemble learning. 

We'll do this through the project Credit Risk Scoring

## 6.1 Credit Risk Scoring project

Let's imagine you want to buy a mobile phone. You go to a bank and want to take a loan from the bank to buy this phone. You fill in some application form that asks for some basic details such as your income, how much the phone cost, how much money you want , do you own a house etc. about you. You fill in the application form. send it to the bank and ask for money. Bank looks at the application and say yes or no. Bank is taking this decision by analyzing the information about you. In this lesson, we want to build a model that the bank can use to make this decision, if they should lend you the money or not. Bank will give to the model how much money you need and so on, basically information about you and model will respond with what is th risk that this customer will not pay back. This is call **default**. The model is going to return the probability or risk that the customer is going to default i.e. **risk of defaulting**. Then the bank can decide based on this risk, whether to lend money to the customer or not.

As a bank we can achieve this by analyzing informations about all the customers that we have.  Bank has all the applications from all the customers and how much money they asked for and which customer was a default and which wern't. Thus it is a binary classification problem $y_{i}= 0 or 1$. 1 is default and 0 is No default.

We want to train a model, so that for each new customer this model will give us a probabilty of default or no default. So $`g(x_{i})`$ will give us the probability of default. X is our feature matrix with all the information about the users that we have. `y` is our target variable.

