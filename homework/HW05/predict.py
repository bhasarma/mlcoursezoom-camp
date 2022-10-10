# predict.py
# Homework 05 | Question 4
# let's serve the model as a webservice using Flask


import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model1.bin' 
dict_vect_file = 'dv.bin'

with open(model_file,'rb') as f_in: 
    model = pickle.load(f_in)

with open(dict_vect_file,'rb') as f_in: 
    dv = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)