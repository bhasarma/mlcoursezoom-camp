'''
Here we'll create a web-services using Flask.
An user will send a request to the address ping
and he will receive PONG in response

How to run: 
1. stay in folder where ping.py is
2. activate conda environment
3. type ipython
4. >> import ping
5. ping.ping()

NEXT: WE WANT TO TRANSFORM THIS FUNCTION INTO A WEBSERVICE
'''

from flask import Flask

app = Flask('ping')

@app.route('/ping', methods = ['GET']) #this is a function decorator. Decorator is a 
#way to add some extra functionalaties to ur function.
# google 'get post web service'. We want to access this function usung the get method

def ping():
	return "PONG"

if __name__=="__main__":
	app.run(debug = True, host='0.0.0.0', port = 9696)