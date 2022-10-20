## 7.2 Building a prediction service with BentoML

In this module, our starting point is the XGboost [model](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/07-bentoml-production/code/train.ipynb) that we created in module 6. We are going to build our prediction service around that model. 

I have run the notebook and got the xgboost model at the end (line 16 in [my notebook](https://github.com/bhasarma/mlcoursezoom-camp/blob/main/WK07-BentoML-production-ready-ML/WEEK-07-notebook.ipynb))

First thing we need to think is: how do we get this model into our ML service and then run it behind an API. **First** thing we have to do is we have to save this model, so that we can load it later in the service. 

In module 5, we talked about pickling a model and then loading it again inside a Flask app. The problem with that approach is that depending on the ML framework there may be specific things that we have to do in order to save it properly. Even within various versions of an individual framework they may recommend different ways saving our model. It is important to look at the documentation and make sure that we are saving the model in a way that the ML framework is recommending. 

What BentoML does is it gives us a simple way of calling a **method**  to save the model. It goes through all of the thing that we have to do depending on the ML framework and depending on the version of that framework and saves it the right way. 

### 7.2.1 Installing BentoML

1. Created a conda environment for this module.

```
(base) bsarma@bsarma-Inspiron-5370:~$ conda create -n bentoml python=3.9

```
2. Activated `bentoml` module

```
(base) bsarma@bsarma-Inspiron-5370:~$ conda activate bentoml
```
Then I entered the `bentoml` environment:
```

(bentoml) bsarma@bsarma-Inspiron-5370:~$

```
3. Installed bentoml with the following command:

```
 
 (bentoml) bsarma@bsarma-Inspiron-5370:~$ pip install bentoml 
 
```
 
 4. Checked the version of bentoml installed (any version with version number 1+ is fine) with:
 
  ```
  (bentoml) bsarma@bsarma-Inspiron-5370:~$ bentoml --version
  ```
 and output is:
 
 `bentoml, version 1.0.7`
 

### 7.2.2
 
Now let's get back to our [jupyter notebook] (https://github.com/bhasarma/mlcoursezoom-camp/blob/main/WK07-BentoML-production-ready-ML/WEEK-07-notebook.ipynb) where model is there.  

As soon as I wanted to import the packages on this jupyter notebook, I noticed that pandas etc. are not installed. It makes sense that I installed them earlier on the `ml-zoomcamp` env and I need to install them again on `bentoml` env. I installed them inside `bentoml` env with the following commnad:

```
conda install numpy pandas scikit-learn seaborn jupyter
```
Now I will try to open the notebook with jupyter. When I imported the packages, I got the error that `No module named 'xgboost`.

Installed it on terminal inside `bentoml` env with the command `pip install xgboost`.

Now I opened notebook again and importing pandas, numpy, sklearn and xgboost worked. 

Then:

* imported `bentoml` with `import bentoml`

* saved model with `bentoml.xgboost.save_model("credit_risk_model", model)`


We wrote service.py

Next in terminal:
``

**References**

1. ML Zoomcamp 7.2 - Building Your Prediction Service with BentoML [youtube](https://www.youtube.com/watch?v=bWdEVlUw1CA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=68) 

2. ML Zoomcamp [notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/07-bentoml-production/code/train.ipynb) for this module.

3. my [notebook](https://github.com/bhasarma/mlcoursezoom-camp/blob/main/WK07-BentoML-production-ready-ML/WEEK-07-notebook.ipynb) for this module