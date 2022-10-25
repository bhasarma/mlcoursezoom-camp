## 7.5 High performance model serving

Here we will see how to test our service with really high volumes of traffic. Then, we will see different optimizations  that we can do to handle high volume traffic. 

In orde to send traffic at our service, we are going to use a tool called `locust`. We'll Install it inside `bentoml` env with command:

```bash
pip install locust
``` 

Then we need `locustfile.py` shown below. It contains a sample of the data that we are going to send. We have to inherit from an `HttpUser`, which is a locust object.  Then within that class we have to create a task and we are calling this class classify. We have to say `self.client.post` to our `classify` endpoint., that's we are going to be sending our `json`. It is just like `swaggerUI`, but in this case `locust` will be running at 10, 100 or even more rps (requests per second). We are defining a `wait_time`, between each time a user calls this `classify`endpoint and we are setting a random time between 0.01 and 2 second, just to give it a little bit of inconsistency. 


```python
#locustfile.py
import numpy as np
from locust import task
from locust import between
from locust import HttpUser

sample = {"seniority": 3,
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

class CreditRiskTestUser(HttpUser):
    """
    Usage:
        Start locust load testing client with:

            locust -H http://localhost:3000

        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn
        rate for the load test from the Web UI and start swarming.
    """

    @task
    def classify(self):
        self.client.post("/classify", json=sample)

    wait_time = between(0.01, 2)

```

To start-up this locust process, we'll call the locust command on terminal:

```bash
locust -H http://localhost:3000
```

Then `locust` has started a local server at ` http://0.0.0.0:8089`, where we'll go in the browser.

However I had had following warning/erroe:
```bash
[2022-10-24 07:47:32,614] bsarma-Inspiron-5370/WARNING/locust.main: System open file limit '1024' is below minimum setting '10000'.
It's not high enough for load testing, and the OS didn't allow locust to increase it by itself.
See https://github.com/locustio/locust/wiki/Installation#increasing-maximum-number-of-open-files-limit for more info.
[2022-10-24 07:47:32,615] bsarma-Inspiron-5370/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
[2022-10-24 07:47:32,635] bsarma-Inspiron-5370/INFO/locust.main: Starting Locust 2.12.2
```
Then I looked [here](https://github.com/locustio/locust/wiki/Installation#increasing-maximum-number-of-open-files-limit) and followed the instructions [here](https://www.tecmint.com/increase-set-open-file-limits-in-linux/).

 However it doesn't work. 
 
 Anyhow, neglecting the above warning, I proceed with locustUI. 

Now in the locust UI it asks: how many users should I start-up and how fast should I start them up (spawn rate), We can set for now to 1 user and 1 user per sec. One thing to **remember** in this case is: default bentoml setting is for a failure is if a request take longer than 1 sec. We can change that, we can change that even to never. But lots of services need a threshold, within which if it can't respond, it sould fail. 

With 50 users and 10 per sec, we get lots of failuers. 

So, we are going to do our first optimization. It is `async` way optimization. 

Sometimes you might have a high failure at the beginning because of the **cold-start** isuue. 



