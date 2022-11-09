#!/usr/bin/env python
# coding: utf-8

import requests

host = 'subscription-serving-env.eba-meke3qbg.us-east-1.elasticbeanstalk.com'
url = f'http://{host}/predict'

#Above two lines are needed if we are running our app on aws_cloud. For local running, below
#url = 'http://localhost:9696/predict'


customer = {

	"Id": 2101,
	"age": 75.0,
	"job": "blue-collar",
	"marital": "married",
	"education": "secondary",
	"default": "no",
	"balance": 100674.0,
	"housing": "yes",
	"loan": "no",
	"contact": "unknown",
	"day": 5,
	"month": "may",
	"duration": 257,
	"campaign": 1,
	"pdays": -1,
	"previous": 0,
	"poutcome": "unknown",
}

requests.post(url, json = customer)


response = requests.post(url, json = customer).json()
print(response)


if response['subscription'] == True:
    print('Customer %s will buy subscription' %(customer['Id']))
else:    
    print('Customer %s will not buy subscription' %(customer['Id']))