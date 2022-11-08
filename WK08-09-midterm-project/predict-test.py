#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'


customer = {

	"Id": 2101,
	"age": 25.0,
	"job": "blue-collar",
	"marital": "married",
	"education": "secondary",
	"default": "no",
	"balance": 674.0,
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