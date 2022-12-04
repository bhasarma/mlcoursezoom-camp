# 10.3 Creating a Preprocessing Service

In this session, we'll start with the jupyter notebook ([link](https://github.com/bhasarma/mlcoursezoom-camp/blob/main/WK13-kubernetes-and-tensorflow-serving/tf-serving-connect.ipynb)) that we did in last session and we'll turn this into a **Flask** application. We used this notebook to communicate with our model deployed with TF-serving. We used this to get an image of a pant, preprocess it, turn it into **protobuf** and then send it to TF-serving, get responses, post-process them and turn it into something humane-readable. Now we want to turn this into a Flask application. 

Before we turn this into a Flask application, we want to turn the notebook into a python script with the command:

```bash
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ jupyter nbconvert --to script tf-serving-connect.ipynb
``` 
Let's rename it to `gateway.py`, because that's what we'll call our service. We have now turned our notebook into a nice looking script. Let's now execute this script. 
```bash

```

 
