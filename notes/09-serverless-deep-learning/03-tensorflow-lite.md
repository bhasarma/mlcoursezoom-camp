## 9.3 TensorFlow Lite

In this lesson, we'll talk about TensorFlow Lite. It is a lighter version of Tensorflow. Plain tensorflow is quite big. Size if the package when unpacked is apprx. 1.7 GBytes and this is too large. There are multiple reasons why we care about size:

- earlier there was limit in AWS Lambda and it was not possible to have a package of 50 MB size. Now, with docker we have larger limits (upto 10 GB). So this reason no longer applies. 

-  We don't want to have a very large image. large image is usually problemetic because we have to pay more for storing large images.  This reason is still not significant, because it is relatively cheap. 

- When we invoke the Lambda function for the first time, it takes some time to initialize the function. With larger image it takes more time. First it needs to download the image, then run it. It is not only slower, but also we have to pay for this time as well. 

- Slower to import, bigger ram footprint: when we do `import tensorflow` it is not instant. It takes some time to import tensorflow,  because it is a large library. It needs to load lots of things. Their **RAM footprint** is also larger. 
 
 Solution to above issues is to use lighter version of tensorflow i.e. tensorflow lite instead of tensorflow. 
 
 Tensorflow LIte focuses only on **inference**. Inference is when we do `model.predict(X)`. This is called inference and tensorflow lite focuses only on it. Tensorflow lite is not used for training models. It is not used for anything else but inference. Only thing that we can do with tensorflow lite is `model.predict(X)` and nothing else. 
 
 To be able to use tensorflow lite, we need to convert the model. 
 
 Now we'll see how to use it. 