## 9.4 Preparing the Code for Lambda

In this session, we'll convert the code we wrote in a notebook in last session into a python script. This time instead of going to File-> Download as, we want to use a command line utility for doing this. It is called **nbconvert** to py. Go to [stack overflow](https://stackoverflow.com/questions/17077494/how-do-i-convert-a-ipython-notebook-into-a-python-file-via-commandline) link on google search.

We convert jupyter notebook into python script with the following command on command line:

```shell
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK-12-serverless-deep-learning$ jupyter nbconvert --to script week12-notebook.ipynb
``` 
Now we have the file `week12-notebook.py`.

Then we cleaned the file, wrote two functions: def predict and def lambda_handler. Then we could run it on our python interface (ipython). 

This works and we get the prediction.

We have actually a problem with this code and we'll see the problem when we try package it later in a docker container. For now it works. 

Before we upload this to lambda, we want to package everything in a docker container, make sure this docker container has tensorflow lite, it has keras image helper, numpy and so on. Next lesson we'll package everything in docker file, then we'll test this docker file locally. 