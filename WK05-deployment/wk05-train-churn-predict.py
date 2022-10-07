#!/usr/bin/env python
# coding: utf-8

# # WEEK 05 | 04.10 - 10.10.2022 | Machine Learning Zoomcamp

# In the previous session we trained a model for predicting churn and evaluated it. Now let's **DEPLOY** it.

# In[1]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


# In[2]:


df = pd.read_csv('data-week-3.csv')

df.columns = df.columns.str.lower().str.replace(' ', '_')

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)

df.churn = (df.churn == 'yes').astype(int)


# In[3]:


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)


# In[4]:


numerical = ['tenure', 'monthlycharges', 'totalcharges']

categorical = [
    'gender',
    'seniorcitizen',
    'partner',
    'dependents',
    'phoneservice',
    'multiplelines',
    'internetservice',
    'onlinesecurity',
    'onlinebackup',
    'deviceprotection',
    'techsupport',
    'streamingtv',
    'streamingmovies',
    'contract',
    'paperlessbilling',
    'paymentmethod',
]


# In[5]:


def train(df_train, y_train, C=1.0):
    dicts = df_train[categorical + numerical].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    
    return dv, model


# In[6]:


def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred


# In[7]:


C = 1.0
n_splits = 5


# In[8]:


kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)

scores = []

for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.churn.values
    y_val = df_val.churn.values

    dv, model = train(df_train, y_train, C=C)
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)

print('C=%s %.3f +- %.3f' % (C, np.mean(scores), np.std(scores)))


# In[9]:


scores


# In[10]:


dv, model = train(df_full_train, df_full_train.churn.values, C=1.0)
y_pred = predict(df_test, dv, model)
y_test = df_test.churn.values
auc = roc_auc_score(y_test, y_pred)
auc


# Now we have this `model` and it still lives in our notebook. We just can't take this model and put it in our webservice. Remember that we want to take this model and put them in a web-service (churn-service) in our case, so that marketing service can use our model to score our customer. We need to be able to use this model. We can't do this from Jupyter notebook. Now we want to save this model in order to be able to load it later to our churn-service. 

# ## Save the model

# In[11]:


import pickle


# * For saving the model we use pickle. It is a built-in library for saving python objects.
# * Now we want to take our model and write it into a file. 
# * first create a file, where we'll write it.

# In[12]:


#output_file = 'model_C=%s.bin' %C
output_file = f'model_C={C}.bin' #a nicer way of writing the previous line using f-strings
output_file


# In[13]:


#we want to create a file with filename output_file.bin and we want to write in this file in binary format
#we aren'T going to write text there. We are going to write bytes there.
f_out = open(output_file, 'wb') 
# we use pcikele to save our model. We use dump function for that
pickle.dump((dv, model), f_out)
# At last we need to close the file. It is very important because, if we don't close the file, we can't be sure,
# if this file has the content and other services can use it.
f_out.close()


# It is very easy accidentally to forget to close the file. That's is better to use the `with` statement. This makes sure that the file is automatically closed all the time. It is automatically closes the file once we go out the `with` statement below. File is `open` as long as we are inside the `with` statement. This is also a bit shorter, 2 lines vs. 3 lines.

# In[14]:


with open(output_file,'wb') as f_out: #this is equivalent to first line in previous block
    pickle.dump((dv, model), f_out)
    # do stuff

#do ohter stuff


# This is how we save the model. Let's see how we load the model. For that, let's restart the current kernel at this point pretending we are in a different and new process now.

# ## Load the model

# In[1]:


import pickle


# Loading the model is preetty similar to saving the model. 

# In[2]:


model_file = 'model_C=1.0.bin' 


# In[3]:


with open(model_file,'rb') as f_in: #
    dv, model = pickle.load(f_in)


# `rb` is very important in above code block. If we don't write `rb` and we write `wb` , it will overwrite the file. It'll create a new file with zero bytes.

# In[4]:


dv, model


# We have our `DictVectorizer` and `LogisticRegression`. This is what we trained and saved previously. We haven't imort scikit-learn here. But we have to have scikit-learn installed in our computer. Without that we'll not get the above output. When it tries to load pickle file in `pickle.load`, it'll complaint that it doesn't know and can't create these classes, it can't create `DictVectorizer` and `LogisticRegression`, because scikit-learn is not installed. 

# Now we have DictVectorizer, model and a "new" customer prepared below, whose score we want to predict.

# In[19]:


#let's create a new customer
customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}


# Let's first turn this customer into a feature matrix.

# In[20]:


X = dv.transform([customer])
X


# In[21]:


model.predict_proba(X)


# In[22]:


model.predict_proba(X)[0,1]


# Now we know how to save the model, how to load the model. But this isn't convenient to do it from Jupyter notebook everytime we want to predict a customer and run all the cells. We just want to have single python file, as script that does that. 

# Now let's download our notebook as a python file.

# In[ ]:




