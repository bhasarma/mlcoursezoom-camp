#code for question 5 of homework 07

import bentoml
import numpy as np
from bentoml.io import JSON
from bentoml.io import NumpyNdarray

from pydantic import BaseModel


class CreditApplication(BaseModel):
	seniority: int
	home: str
	time: int
	age: int
	marital: str
	records: str
	job: str
	expenses: int 
	income: float
	assets: float
	debt: float
	amount: int
	price: int


model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
#dv = model_ref.custom_objects['dictVectorizer']
  

model_runner = model_ref.to_runner()

 

svc = bentoml.Service("mlzoomcamp_classifier", runners = [model_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray()) 
def classify(vector):	
	prediction = model_runner.predict.run(vector)
	print(prediction)

	result = prediction[0]
	print("here comes result")
	print(type(prediction))
	print(result)
	
	return(prediction)