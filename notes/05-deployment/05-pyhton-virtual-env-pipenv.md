# Python Virtual Environment: Pipenv

## Installing pipenv

`$ pip install pipenv`

on windows also it is the same.
Install it on the the folder where your train.py, model.bin, predict.py etc wre there. 

## Installing packages with pipenv
- Now in order to install a package, we stay inside the same folder and install the package using:

`$ pipenv install numpy scikit-learn==0.24.2 flask`

It creates two files Pipfile and Pipfile.lock.

 - Also install gunicorn (if you are on windows install waitress)
 
 `$ pipenv install gunicorn`
 
 We save everything to git.  If our colleague wants to work with it, he clones this repo on his computer. What they do after cloning is, they just do:
 
 `$ pipenv install`.
 
 That's all they need to do. They don't need to write all the names of the libraries. Pinenv will use the Pipfile and Pipfile.lock to figure our which dependencies it needs. 
 
## Running our service

get inside the environment with:

`$ pipenv shell`

It shows which folder it is using for storing the virtual environment.

`$ gunicorn --bind 0.0.0.0:9696 predict:app`

Instead of above two commands we can also write:

`$ pipenv run gunicorn --bind 0.0.0.0:9696 predict:app`