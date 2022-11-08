#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
from sklearn.metrics import roc_auc_score

# parameters

eta = 0.1
max_depth = 6
min_child_weight = 10
output_file = 'model.bin'


# data preparation
df = pd.read_csv('predict-term-deposit-data.csv')

df.columns = df.columns.str.lower()


## converting `day` and `month` into `day_of_year`
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
        year='2055',
        month=df['month'], 
        day=df['day']
    )
)

df['day_of_year']=df['date_formatted'].dt.dayofyear


df = df.drop(columns = ['id','day','month','date_formatted'])


df.default = (df.default == 'yes').astype(int)
df.housing = (df.housing == 'yes').astype(int)
df.loan = (df.loan == 'yes').astype(int)
df.y = (df.y == 'yes').astype(int)


# Splitting full dataset into train, validation and test datasets

df_full_train, df_test = train_test_split(df, test_size = 0.2, random_state = 11)


df_full_train = df_full_train.reset_index(drop = True)
df_test = df_test.reset_index(drop = True)


y_full_train = df_full_train.y.values
y_test = df_test.y.values


del df_full_train['y']
del df_test['y']


# Dealing with -1 values in pdays

df_test['pdays'] = df_test['pdays'].replace([-1], 999999999)
df_full_train['pdays'] = df_full_train['pdays'].replace([-1], 999999999)


df_full_train['age'] = df_full_train['age'].replace([-1, 999], df_full_train['age'].mode()[0])
df_test['age'] = df_test['age'].replace([-1, 999], df_test['age'].mode()[0])


# Dealing with Missing Values


df_full_train['age'] = df_full_train['age'].fillna(df_full_train['age'].mode()[0])
df_test['age'] = df_test['age'].fillna(df_test['age'].mode()[0])

df_full_train['balance'] = df_full_train['balance'].fillna(df_full_train['balance'].mode()[0])
df_test['balance'] = df_test['balance'].fillna(df_test['balance'].mode()[0])



cols_numerical = list(df_full_train.select_dtypes(include='number').columns)
cols_categorical = list(df_full_train.select_dtypes(exclude='number').columns)



# One hot encoding
dv = DictVectorizer(sparse = False)

full_train_dict = df_full_train.to_dict(orient='records')
test_dict = df_test.to_dict(orient='records')


X_full_train = dv.fit_transform(full_train_dict)
X_test = dv.transform(test_dict)

features = dv.get_feature_names()
dfulltrain = xgb.DMatrix(X_full_train, label=y_full_train, feature_names=features)
dtest = xgb.DMatrix(X_test, feature_names=features)



# Training: Gradient boosting with XGBoost 

print(f'training the xgboost model with eta={eta}, max_depth={max_depth} and min_child_weight={min_child_weight}')
xgb_params = {
    'eta': eta,    
    'max_depth': max_depth,
    'min_child_weight': min_child_weight,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    #'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}
model = xgb.train(xgb_params, dfulltrain, num_boost_round=190)
y_pred = model.predict(dtest)
print('Result of Final Gradient Boosting Model:')
print(f'ROC AUC score: {roc_auc_score(y_test, y_pred).round(3)}')


# saving the file with pickle
with open(output_file,'wb') as f_out: 
    pickle.dump((dv, model), f_out)


print(f'the model is saved to {output_file}')