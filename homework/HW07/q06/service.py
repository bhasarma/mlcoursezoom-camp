import numpy as np
import bentoml
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


#model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5") #second model
model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
#dv = model_ref.custom_objects['dictVectorizer']
model_runner = model_ref.to_runner()

svc = bentoml.Service("credit_risk_classifier", runners=[model_runner])

@svc.api(input=NumpyNdarray(), output=JSON())
async def classify(vector):    
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)
    result = prediction[0]
    if result > 0.5:
        return {
            "status": "DECLINED"
        }
    elif result > 0.25:
        return {
            "status": "MAYBE"
        }
    else:
        return {
            "status": "APPROVED"
        }