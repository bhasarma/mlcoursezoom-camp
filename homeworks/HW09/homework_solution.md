## Homework

In this homework, we'll deploy the dino or dragon model we trained in the 
[previous homework](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/08-deep-learning/homework.md).

Download the model from here: 

https://github.com/SVizor42/ML_Zoomcamp/releases/download/dino-dragon-model/dino_dragon_10_0.899.h5

***Downloaded*** the model with the command from terminal:
```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/homework/HW09$ wget https://github.com/SVizor42/ML_Zoomcamp/releases/download/dino-dragon-model/dino_dragon_10_0.899.h5 -O dino-or-dragon.h5

(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/homework/HW09$ ls
dino-or-dragon.h5

(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/homework/HW09$ ls -lh
total 86M
-rw-rw-r-- 1 bsarma bsarma  86M Nov 19 19:23 dino-or-dragon.h5
-rw-rw-r-- 1 bsarma bsarma 5.1K Nov 27 17:43 homework.md
```


## Question 1

Now convert this model from Keras to TF-Lite format.

What's the size of the **converted** model?

* 21 Mb
* 43 Mb
* 80 Mb
* 164 Mb

### Answer to question 1
`43 Mb` (look into homework09.ipynb file for reference)

## Question 2

To be able to use this model, we need to know the index of the input and 
the index of the output. 

What's the output index for this model?

* 3
* 7
* 13
* 24

### Answer to question 2
`13` (look into homework09.ipynb file for reference)

## Preparing the image

You'll need some code for downloading and resizing images. You can use 
this code:

```python
from io import BytesIO
from urllib import request

from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img
```

For that, you'll need to have `pillow` installed:

```bash
pip install pillow
```

Let's download and resize this image: 

https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px-Smaug_par_David_Demaret.jpg

Based on the previous homework, what should be the target size for the image?


## Question 3

Now we need to turn the image into numpy array and pre-process it. 

> Tip: Check the previous homework. What was the pre-processing 
> we did there?

After the pre-processing, what's the value in the first pixel, the R channel?

* 0.3353411
* 0.5529412
* 0.7458824
* 0.9654902


### Answer to question 3
`0.5529412` (look into homework09.ipynb file for reference)

## Question 4

Now let's apply this model to this image. What's the output of the model?

* 0.17049132
* 0.39009996
* 0.60146114
* 0.82448614

### Answer to question 4
`0.82448614` (look into homework09.ipynb file for reference)

## Prepare the lambda code 

Now you need to copy all the code into a separate python file. You will 
need to use this file for the next two questions.

Tip: you can test this file locally with `ipython` or Jupyter Notebook 
by importing the file and invoking the function from this file.  


## Docker 

For the next two questions, we'll use a Docker image that we already 
prepared. This is the Dockerfile that we used for creating the image:

```docker
FROM public.ecr.aws/lambda/python:3.9
COPY dino-vs-dragon-v2.tflite .
```

And pushed it to [`svizor42/zoomcamp-dino-dragon-lambda:v2`](https://hub.docker.com/r/svizor42/zoomcamp-dino-dragon-lambda/tags).

A few notes:

* The image already contains a model and it's not the same model
  as the one we used for questions 1-4.
* The version of Python is 3.9, so you need to use the right wheel for 
  TF-Lite. For Tensorflow 2.7.0, it's https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl





## Question 5

Download the base image `svizor42/zoomcamp-dino-dragon-lambda:v2`. You can easily make it by using [docker pull](https://docs.docker.com/engine/reference/commandline/pull/) command.

So what's the size of this base image?

* 139 Mb
* 329 Mb
* 639 Mb
* 929 Mb

You can get this information when running `docker images` - it'll be in the "SIZE" column.

### Answer to question 5
```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/homework/HW09$ docker build -t mlzoomcamp-hw09 .

(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/homework/HW09$ docker image ls -a

svizor42/zoomcamp-dino-dragon-lambda                                  v2                               20ef58b21a05   9 days ago       639MB
```

## Question 6

Now let's extend this docker image, install all the required libraries
and add the code for lambda.

You don't need to include the model in the image. It's already included. 
The name of the file with the model is `dino-vs-dragon-v2.tflite` and it's 
in the current workdir in the image (see the Dockerfile above for the 
reference).

Now run the container locally.

Score this image: https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg

What's the output from the model?

* 0.12
* 0.32
* 0.52
* 0.72

### Answer to question 6
Step 1: build docker image with:

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/homework/HW09$ docker build -t mlzoomcamp-hw-serverless .
```
step2: run docker image with:

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/homework/HW09$ docker run -it --rm -p 8080:8080 mlzoomcamp-hw-serverless
```

step3: open a new terminal in the same dir where homework09.py, Dockerfile and test.py is. Then run test.py as below:

```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/homework/HW09$ python test.py 
{'prediction': 0.3195067048072815}
```
Thus answer is : `0.32`

## Publishing it to AWS

Now you can deploy your model to AWS!

* Publish your image to ECR
* Create a lambda function in AWS, use the ECR image
* Give it more RAM and increase the timeout 
* Test it
* Expose the lambda function using API Gateway

This is optional and not graded.


## Publishing to Docker hub

This is just for reference, this is how we published our image to Docker hub:

```bash
docker build -t zoomcamp-dino-dragon-lambda .
docker tag zoomcamp-dino-dragon-lambda:latest svizor42/zoomcamp-dino-dragon-lambda:v2
docker push svizor42/zoomcamp-dino-dragon-lambda:v2
```


## Submit the results

* Submit your results here: https://forms.gle/Pnx563ELg9jgjxHX6
* You can submit your solution multiple times. In this case, only the last submission will be used 
* If your answer doesn't match options exactly, select the closest one


## Deadline

The deadline for submitting is **28 November 2022 (Monday), 23:00 CEST (Berlin time)**. 

After that, the form will be closed.
