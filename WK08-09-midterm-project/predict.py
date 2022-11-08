'''
Here we take predict.py and create a subscription service (web-service) using flask
'''
import pickle

from flask import Flask
from flask import request
from flask import jsonify

from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb


model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('subscription')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    dx = xgb.DMatrix(X, feature_names=dv.get_feature_names())
    y_pred = model.predict(dx).round(3)
    subscription = y_pred >= 0.5 

    result = {
        'subscription_probability': float(y_pred),
        'subscription': bool(subscription)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)