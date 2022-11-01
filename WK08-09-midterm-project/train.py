#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

data = 'https://raw.githubusercontent.com/bhasarma/mlcoursezoom-camp/main/WK08-09-midterm-project/predict-term-deposit-data.csv'
#!wget $data  #uncomment it, if you haven't downoaded data already.

df = pd.read_csv('predict-term-deposit-data.csv')


df.columns = df.columns.str.lower()


df['day'] = df['day'].map(str)
month_mapping = {
    'jan': '1',
    'feb': '2',
    'mar': '3',
    'apr': '4',
    'may': '5',
    'jun': '6',
    'jul': '7', 
    'aug': '8', 
    'sep': '9',
    'oct': '10', 
    'nov': '11', 
    'dec': '12' 
}
df['month'] = df['month'].map(month_mapping)


df['date_formatted'] = pd.to_datetime(
    dict(         
        year='2025',
        month=df['month'], 
        day=df['day']
    )
)

df['day_of_year']=df['date_formatted'].dt.dayofyear



df = df.drop(columns = ['id','day','month','date_formatted'])

df.y = (df.y == 'yes').astype(int)



#splitting the data
df_full_train, df_test = train_test_split(df, test_size = 0.2, random_state = 11)
df_train, df_val = train_test_split(df_full_train, test_size = 0.25, random_state = 11)


df_train = df_train.reset_index(drop = True)
df_val   = df_val.reset_index(drop = True)
df_test = df_test.reset_index(drop = True)

y_train = df_train.y.values
y_val = df_val.y.values
y_test = df_test.y.values
y_full_train = df_full_train.y.values


del df_train['y']
del df_val['y']
del df_test['y']
del df_full_train['y']


df_train['pdays'] = df_train['pdays'].replace([-1], '999999999')
df_test['pdays'] = df_test['pdays'].replace([-1], '999999999')
df_val['pdays'] = df_val['pdays'].replace([-1], '999999999')
df_full_train['pdays'] = df_full_train['pdays'].replace([-1], '999999999')


df_train['age'] = df_train['age'].fillna(0)
df_val['age'] = df_val['age'].fillna(0)
df_test['age'] = df_test['age'].fillna(0)
df_full_train['age'] = df_full_train['age'].fillna(0)

df_train['balance'] = df_train['balance'].fillna(0)
df_val['balance'] = df_val['balance'].fillna(0)
df_test['balance'] = df_test['balance'].fillna(0)
df_full_train['balance'] = df_full_train['balance'].fillna(0)





train_dicts = df_train.to_dict(orient = 'records') #let's turn it into a dict
dv = DictVectorizer(sparse = False)
X_train = dv.fit_transform(train_dicts)


model = LogisticRegression(solver="liblinear", C=1.0, max_iter=1000, random_state=42)
model.fit(X_train, y_train)


val_dicts = df_val.to_dict(orient='records')
X_val = dv.transform(val_dicts)


y_pred = model.predict_proba(X_val)[:,1]


above_average_predict = (y_pred >= 0.5).astype(int)


y_pred_binary = above_average_predict



accuracy = (y_pred_binary == y_val).mean()


# save the model
output_file = 'model.bin' 
with open(output_file,'wb') as f_out:
    pickle.dump((dv, model), f_out)
