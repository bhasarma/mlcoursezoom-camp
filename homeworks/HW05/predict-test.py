#predict-test.py
#Homework 05 | Question 4 and Question 6
#let's serve the model as a webservice using Flask in Q4
# Docker container in Q5

import requests

url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
#client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}  #for q4
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"} #for q6

response = requests.post(url, json = client).json() 
print(response)


if response['churn'] == True:
    print('sending promo email to %s' %('xyz-123'))
else:
    print('not sending promo email to %s' % customer_id)
