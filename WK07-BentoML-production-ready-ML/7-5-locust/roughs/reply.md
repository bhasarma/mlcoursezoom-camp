

## Points discussed:
1. What’s appearing in your bentoml console? Quite possibly you will find errors logged there that help you find the issue.

- Bentoml console appears to be fine. A scrennshot below. I think, therefore no question of errors at this stage.

2. Test the service first by just sending a single request using curl or swagger.
- since bentoml is working fine, this means, a single request should be fine as well.

3. Content of my locustfile and that of Euge is exactly same, accept that he is sending an array and I am sending a json.

4. He got some more errors like `'list' object has no attribute 'items'`, but  don't have this error.

5. Make sure you return  the result from your function in service.py.

- I have returned result from service.py

6. Your service.py is incorrect. It needs to be updated to handle NumpyNdarray().
- I shouldn't update it to NUmpyNdarray, because my output is json. 
