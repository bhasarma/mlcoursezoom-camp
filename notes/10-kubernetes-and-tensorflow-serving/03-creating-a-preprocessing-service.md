# 10.3 Creating a Preprocessing Service

In this session, we'll start with the jupyter notebook ([link](https://github.com/bhasarma/mlcoursezoom-camp/blob/main/WK13-kubernetes-and-tensorflow-serving/tf-serving-connect.ipynb)) that we did in last session and we'll turn this into a **Flask** application. We used this notebook to communicate with our model deployed with TF-serving. We used this to get an image of a pant, preprocess it, turn it into **protobuf** and then send it to TF-serving, get responses, post-process them and turn it into something humane-readable. Now we want to turn this into a **Flask application**. 

Before we turn this into a Flask application, we want to turn the notebook into a python script with the command:

```bash
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ jupyter nbconvert --to script tf-serving-connect.ipynb
``` 
Let's rename it to `gateway.py`, because that's what we'll call our service. We have now turned our notebook into a nice looking script. Let's now execute this script. Before that, first we have to run docker again, that I closed after the 10.2 session.

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ docker run -it --rm -p 8500:8500 -v "$(pwd)/clothing-model:/models/clothing-model/1" -e MODEL_NAME="clothing-model" tensorflow/serving:2.7.0
```

Then, open another terminal and run `gateway.py`

```bash
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ python gateway.py
```
 We got the following output:
 
 {'dress': -1.8682903051376343, 'hat': -4.761245250701904, 'longsleeve': -2.316983461380005, 'outwear': -1.0625708103179932, 'pants': 9.887161254882812, 'shirt': -2.8124334812164307, 'shoes': -3.6662826538085938, 'shorts': 3.200361728668213, 'skirt': -2.6023378372192383, 't-shirt': -4.835046291351318}


Now we want to turn this spcript into a **Flask application**. For this we can refer to `predict.py` of module 5 in this [here](https://github.com/bhasarma/mlcoursezoom-camp/tree/main/WK05-deployment).

Now also let's prepare a test.py file. We can copy it from previous module (module 9). 

Now we are running `docker run...` in one terminal, `python gateway.py` in another terminal with flask application in it and `python test.py` in third temrinal. 

Now, we want to put it in pipenv. this is something we'll need while preparing the images. We'll need to install a bunch of things. 

```
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ pipenv install grpcio==1.42.0 flask==2.1.3 gunicorn keras-image-helper
```
We are not installing tensorflow and TF-serving here. We are using only one function from tensoflow i.e tf.mkae_tensor_proto(). Only for this we are carrying tensorflow with 1.7 Gb. There is a lighter weight tensorflow.  Its clalled `tensorflow-cpu`. It is smaller than normal `tensor-flow`. But still 400 Mb or somethig like this. We only need to have make_tensor_proto for converting numpy into protobuf format. Gettin the entire library for t is too much. We have solution for this problem as well. It is `tensorflow_protobuf`. Alexey wrote a script that extrctats all the protobuf files and puts them separately. It still used the tensorflow package, but only keeps the protobuf file that we need. 

```
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ pipenv install tensorflow-protobuf==2.7.0

``` 
This is instead of tensorflow, or tensorflow-cpu or tensorflow-serving-api.


