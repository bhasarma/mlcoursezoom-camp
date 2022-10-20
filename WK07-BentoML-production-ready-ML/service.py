import bentoml

from bentoml.io import JSON

#pulling our model in
# a model reference take in the unique tag that we created in notebook and it pulls in all the metadata that we created
# for that model. We'll use the model reference to get variety of things.

#model_ref = bentoml.xgboost.get("credit_risk_model:waipffspxclivn6r") #model that gave error due to dictVectorizer 
#model_ref = bentoml.xgboost.get("credit_risk_model:ztgcukspx6livn6r")
model_ref = bentoml.xgboost.get("credit_risk_model:latest") #pulls latest model from local repo
dv = model_ref.custom_objects['dictVectorizer']

#Getting access to the model
# model_ref.to_runner is bentoml's abstraction for model_runner itself. We'll see how to use it in a minute. 
# this abstraction layer allows us to scale the model separately from the rest of the service. We'll get into
# different high-performing scenarios where it applies. For now, it is a way for us to access the model and predict.  

model_runner = model_ref.to_runner()

# next things we are going to do is we are going to create our service. 

svc = bentoml.Service("credit_risk_classifier", runners = [model_runner])

@svc.api(input=JSON(), output=JSON())
def classify(application_data):
	vector = dv.transform(application_data)
	prediction = model_runner.predict.run(vector)
	print(prediction)
	return {"status": "Approved"}