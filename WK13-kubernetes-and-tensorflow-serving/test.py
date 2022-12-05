import requests

url = 'http://localhost:9696/predict'

#for aws lamda deplyment. Below is the url we got from API Gateway
#url = 'https://c8m95kkqv5.execute-api.us-east-1.amazonaws.com/test/predict' 

data = {'url': 'http://bit.ly/mlbookcamp-pants'}


result = requests.post(url, json=data).json()
print(result)