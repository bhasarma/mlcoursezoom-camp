#write a script for loading models with pickle

import pickle

model_file = 'model1.bin' 
dict_vect_file = 'dv.bin'
with open(model_file,'rb') as f_in: 
    model = pickle.load(f_in)

with open(dict_vect_file,'rb') as f_in: 
    dv = pickle.load(f_in)

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

X = dv.transform([client])
y_pred = model.predict_proba(X)[0,1]

print('input', client)
print('churn probability', y_pred)