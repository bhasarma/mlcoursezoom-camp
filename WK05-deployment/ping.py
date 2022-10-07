from flask import Flask

app = Flask('ping')

@app.route('/ping', methods = ['GET']) #this is a function decorator. Decorator is a 
#way to add some extra functionalaties to ur function.
# google 'get post web service'. We want to access this function usung the get method
def ping():
	return "PONG"

if __name__=="__main__":
	app.run(debug = True, host='0.0.0.0', port = 9696)