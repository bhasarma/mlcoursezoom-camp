## 7.4 Sendng. receiving and validating data

As we are sending, receiving and cleaning data, we'll be playing with lots of data. In the previous modules, we played read data from a .csv file, cleaned it and did a lot of transformations on it. We are going to see today how to deal with a couple of different datatypes, validate them and make sure that we are getting the right thing from the person who is sending us the data.

The json data that bentoml is receiving till now is raw json data. It looked like:

```json

{"seniority": 3,
"home": "owner",
"time": 36,
"age": 26,
"marital": "single",
"records": "no",
"job": "freelance",
"expenses": 35,
"income": 0.0,
"assets": 60000.0,
"debt": 3000.0,
"amount": 800,
"price": 1000
}
```

what if if we send something without `expenses` or something is that is just a random datapoint or, really our data point is messed up. This happens often with data like below:

```json
{"seniority": 3,
"home": "owner",
"time": 36,
"age": 26,
"marital": "single",
"records": "no",
"asdf": "freelance",
"income": 0.0,
"assets": 60000.0,
"debt": 3000.0,
"price": 1000
}
``` 

The **problem** is that it ddnt fail. It returned something that might have been a valid answer. That's worser than failing. 


What we want to do here is: we want to really fail, if the data that is sent to us doesn't look right. This is where a libraray called **pydantic** comes in. It is implemented by Bentoml and automatically imported as a dependency of Bentoml. We will see how to create a pydantic schemer to validate the incoming data. 

First we'll import it as `from pydantic import BaseModel`in the `service.py` file.  The class `BaseModel` is actually a `pydantic` class that we need to extend in order to create a data schemer. We will see what is a data schemer. 

Now I run on  terminal `betoml build`. I get error: `Error: [bentoml-cli] `build` failed: Failed to import module "service": No module named 'pydantic'`

Solution: 
installed pydantic in bentoml env with ` pip install pydantic`

Then I ran the new service.py and bentofile.yaml with `bentoml serve service.py:svc --reload`.

When all datas are as expected, then we don't get any error. But if one field e.g. `marital` is missing,  I got the error `bentoml.exceptions.BadInput: Invalid JSON input received: 1 validation error for CreditApplication
marital`.

So it will give us error, if any of the data is not in the way, we expect them to be. **VERY NICE**.

Now we'll see a couple of other different types of data, that we can send.  
