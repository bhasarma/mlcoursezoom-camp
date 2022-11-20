# 8.2 Tensorflow and Keras

Tensorflow is a library (more like a framework) for doing deeplearning. It is an end-to-end open source machine learning platform.  It can do other things, but main focus for this library is deep learning. So, Tensorflow is a library for training deep learning models. 

Keras is a higher level abstraction on top of tensorflow. Inside Tensorflow, we have Keras, which is a libraray. It provides higher level abstraction which helps to create, train and use neural networks. Officila website of tensorflow is: [https://www.tensorflow.org/] (https://www.tensorflow.org/).

**Installing Tensorflow**
Tensorflow doesn't come with Anaconda. If we use Anaconda, we don't have tensorflow.

Install it from inside of Jupyter notebook with : `!conda install tensorflow -y`

If you are doing it from jupyter, you need `-y` at the end. Then it doesn't asks confirming to install.

Alternatively, you can install it with `!pip install tensorflow` 


But in this module, I am working on Jupyter noteook with GPU in Saturn. I don't have to install TensorFlow. I can there directly import TensorFlow with:

```
import tensorflow as tf
tf.__version__
'2.9.1'
```

Saturn has tensorflow and everything else configured. Same with Amazon Sagemaker, at least at the time when Video was recorded. 

On your local computer, if you don't have a GPU, you install it as above written. If you have a GPU, it is little bit more complex. Some links will be shared to us. It is always better to use cloud solution, where everything is configured and we don't have to worry about it. We can just use a notebook and start training our model.

Keras used to be a separate library from TensorFlow. Sometime it got absorbed into TensorFlow. If on some online tutorial, you see that `keras.preprocessing.image` then just put a `tensorflow.` before. From TensorFlow version `2.0` it is true. We should use atleast a `2.0` version of TensorFlow.

The libraray for processing images is PIL, stands for python image libraray. Many libraries use this for processing images. 

- dtype=uint8 means unsigned. SO it goes from 0 t 255, not from -127 to 128, but from 0 to 255. int8 means that it is an integer that takes 8 bits or 1 byte. 