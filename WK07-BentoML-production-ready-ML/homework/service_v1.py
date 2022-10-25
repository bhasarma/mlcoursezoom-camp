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


model_ref = bentoml.sklearn.get("mlzoomcamp_homework:latest")
#dv = model_ref.custom_objects['dictVectorizer']
  

model_runner = model_ref.to_runner()

 

svc = bentoml.Service("mlzoomcamp_classifier", runners = [model_runner])

@svc.api(input=NumpyNdarray(), output=JSON()) 
def classify(vector):	
	prediction = model_runner.predict.run(vector)
	print(prediction)

	result = prediction[0]
	print("here comes result")
	print(result)
	
	if result > 0.5:
		return {"status": "DECLINED"}
	elif result > 0.23:
		return {"status": "NOT AT ALL"}
	else:
		return {"status": "APPROVED"}