'''
Here we take predict.py and create a subscription service (web-service) using flask
'''
import pickle

from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb


model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


customer = {
    'age': 25.0,
    'job': 'blue-collar',
    'marital': 'married',
    'education': 'secondary',
    'default': 'no',
    'balance': 11674.0,
    'housing': 'yes',
    'loan': 'no',
    'contact': 'unknown',
    'day': 5,
    'month': 'may',
    'duration': 257,
    'campaign': 1,
    'pdays': -1,
    'previous': 0,
    'poutcome': 'yes',
}


X = dv.transform([customer])
dx = xgb.DMatrix(X, feature_names=dv.get_feature_names())
y_pred = model.predict(dx)

print('input:', customer)
print('subscription probability:', y_pred)