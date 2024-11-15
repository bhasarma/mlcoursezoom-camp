# Homework 05 | WEEK 05 (04.10-10.10.2022) | Machine Learning Zoomcamp

Linke to the homework [here](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/05-deployment/homework.md)

## Dataset 

* same credit card dataset as in the previous homework
* Credit Card Data from book "Econometric Analysis".
* Here's a wget able link:
```{bash}
wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/AER_credit_card_data.csv
```

## Question 1

* Install Pipenv
* What's the version of pipenv you installed?
* Use `--version` to find out

![Imgur](https://i.imgur.com/8iYJHtX.png)
 **Figure 1**: `pipenv` installed and its ersion is `2022.10.4`
 
 **Answer to question 1**
 
 `2022.10.4`
 
## Question 2

* Use Pipenv to install Scikit-Learn version 1.0.2
* What's the first hash for scikit-learn you get in Pipfile.lock?

Note: you should create an empty folder for homework and do it there.

![Imgur](https://i.imgur.com/xRzo7jp.png)
**Figure 2**: pipenv is used to install Scikit-Learn version 1.0.2 using the command `pipenv install scikit-learn==1.0.2`.

**Answer to question 2**
First hash for scikit-learn we get in `Pipfile.lock` is `"sha256": "c71abaddf023d2d7029f36beec9b8afb73c91860ff0002758fa66f8ea365dad0"`


## Models
We've prepared a dictionary vectorizer and a model.

They were trained (roughly) using this code:

```
features = ['reports', 'share', 'expenditure', 'owner']
dicts = df[features].to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)

model = LogisticRegression(solver='liblinear').fit(X, y)
```

Note: You don't need to train the model. This code is just for your reference.
And then saved with Pickle. Download them:

* [DictVectorizer](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/05-deployment/homework/dv.bin?raw=true)
* [LogisticRegression](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/05-deployment/homework/model1.bin?raw=true)

With wget:
```
PREFIX=https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/course-zoomcamp/cohorts/2022/05-deployment/homework
wget $PREFIX/model1.bin
wget $PREFIX/dv.bin
```

## Question 3
Let's use these models!

* Write a script for loading these models with pickle
* Score this client:
`{"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}`

What's the probability that this client will get a credit card?

* 0.162
* 0.391
* 0.601
* 0.993

If you're getting errors when unpickling the files, check their checksum:

```
$ md5sum model1.bin dv.bin
3f57f3ebfdf57a9e1368dcd0f28a4a14  model1.bin
6b7cded86a52af7e81859647fa3a5c2e  dv.bin
```
Solution:

```{python}
# write a script for loading models with pickle
# q3.py
import pickle

model_file = 'model1.bin' 
dict_vect_file = 'dv.bin'
with open(model_file,'rb') as f_in: 
    model = pickle.load(f_in)

with open(dict_vect_file,'rb') as f_in: 
    dv = pickle.load(f_in)

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

X = dv.transform([client])
y_pred = model.predict_proba(X)[0,1]

print('input', client)
print('churn probability', y_pred)

```
![Imgur](https://i.imgur.com/eajHHNE.png)
**Figure3**: output of q3.py

**Answer to question 3**
`0.162`

## Question 4

Now let's serve this model as a web service

* Install Flask and gunicorn (or waitress, if you're on Windows)
* Write Flask code for serving the model
* Now score this client using `requests`:

```
url = "YOUR_URL"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
requests.post(url, json=client).json()
```

What's the probability that this client will get a credit card?

* 0.274
* 0.484
* 0.698
* 0.928

Solution:

![Imgur](https://i.imgur.com/0PTB9Vp.png)
**Figure4**: installation of flask and gunicorn 

** Flask code for serving the model**

```{python}
# predict.py
# Homework 05 | Question 4
# let's serve the model as a webservice using Flask


import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model1.bin' 
dict_vect_file = 'dv.bin'

with open(model_file,'rb') as f_in: 
    model = pickle.load(f_in)

with open(dict_vect_file,'rb') as f_in: 
    dv = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

```
Then, 

`$ pipenv shell`

`$ gunicorn --bind 0.0.0.0:9696 predict:app `

or in one line,

`pipenv run gunicorn --bind 0.0.0.0:9696 predict:app`

![Imgur](https://i.imgur.com/d2XTlPJ.png)
**Figure 5**: 

![Imgur](https://i.imgur.com/6m3G8pu.png)
**Figure 6**: 

```{python}
#predict-test.py
#Homework 05 | Question 4
#let's serve the model as a webservice using Flask

import requests

url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}


response = requests.post(url, json = client).json() 
print(response)


if response['churn'] == True:
    print('sending promo email to %s' %('xyz-123'))
else:
    print('not sending promo email to %s' % customer_id)
```

**Answer to question 4**

`0.928`
***



### Docker
Install [Docker](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/05-deployment/06-docker.md). We will use it for the next two questions.

For these questions, we prepared a base image: `svizor/zoomcamp-model:3.9.12-slim`. You'll need to use it (see Question 5 for an example).

This image is based on `python:3.9.12-slim` and has a logistic regression model (a different one) as well a dictionary vectorizer inside.

This is how the Dockerfile for this image looks like:

```{dockerfile}
FROM python:3.9.12-slim
WORKDIR /app
COPY ["model2.bin", "dv.bin", "./"]
```

We already built it and then pushed it to `svizor/zoomcamp-model:3.9.12-slim`.

Note: You don't need to build this docker image, it's just for your reference.

## Question 5
Download the base image `svizor/zoomcamp-model:3.9.12-slim`. You can easily make it by using `docker pull` command.

So what's the size of this base image?

* 15 Mb
* 125 Mb
* 275 Mb
* 415 Mb

You can get this information when running `docker images` - it'll be in the "SIZE" column.

Solution:

* docker installed using command `sudo apt-get install docker.io `on directory `(base) bsarma@bsarma-Inspiron-5370:~/GitHub/mlcoursezoom-camp/homework/HW05$ `

* Then, download the base image using the command `sudo docker pull svizor/zoomcamp-model:3.9.12-slim` in directory `(base) bsarma@bsarma-Inspiron-5370:~/GitHub/mlcoursezoom-camp/homework/HW05$ `

* Then typed `sudo docker images` on the same directory as above and got the following output.

![Imgur](https://i.imgur.com/xL2b3T2.png)
**figure 7**:

**Answer to question 5**

`125 MB`
***

## Dockerfile
Now create your own Dockerfile based on the image we prepared.

It should start like that:
```{dockerfile}
FROM svizor/zoomcamp-model:3.9.12-slim
# add your stuff here

```
Now complete it:

* Install all the dependencies form the Pipenv file
* Copy your Flask script
* Run it with Gunicorn
* After that, you can build your docker image.

## Question 6

Let's run your docker container!

After running it, score this client once again:

```{python}
url = "YOUR_URL"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
requests.post(url, json=client).json()
```

What's the probability that this client will get a credit card now?

* 0.289
* 0.502
* 0.769
* 0.972

Solution:

**Writing the `Dockerfile`**
```{dockerfile}
FROM svizor/zoomcamp-model:3.9.12-slim


RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]


RUN pipenv install --system --deploy

COPY ["predict.py","./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]

```
 

* step 1:  `sudo docker build -t svizor/zoomcamp-model .` on `(base) bsarma@bsarma-Inspiron-5370:~/GitHub/mlcoursezoom-camp/homework/HW05$` directory

![Imgur](https://i.imgur.com/ppSqCwm.png)

**Figure8**: Building docker images after completing the `Dockerfile`

* step2:  `sudo docker run -it --rm -p 9696:9696 svizor/zoomcamp-model` on same dir. as in step 1

![Imgur](https://i.imgur.com/lVjX0zy.png)
**Figure 9**: running docker container after building it in step 1 above

* step3: `python predict-test.py` on another terminal but in the same directory as in previous steps.

![Imgur](https://i.imgur.com/i6WrkRO.png)
**Figure 10**: output of `predict-test.py` after running docker container as in step 2 above.

**Answer to question 6**

`0.769`