In this lesson we'll talk about transfer learning.

In the previous lesson, we talked about internals of neural networks. We talked about convolutional layers. Main purpose of convolutional layer is to convert image into a vector representationn  of the image by using one layer after another, each layer consisting of number of filters. 

Then we talked about dense layers. They take vector representation and use it for making prediction. 

In this lesson we'll see how to use a neural network, already trained on imagenet dataset. This NN contains filters in each layer. These filters are learnable. Model learns these filters during training. Filters they learn are quite generic. They can be used for many purposes. Somebody trained these network on imagenet. They trained bunch of filters. Model learn to take image in a picture and convert it into some vector representation. This is quite generic. We don't need to change it for our task. Actually training these filters for convolutional layers is very difficult. We need to have lots of images. Model needs to see a lots of images to come up with filters that makes sense. Model needs to see huge amounts of images to be able to come up with filters like that. 

Then we have bunch of dense layers. After we convert image into vector representation, we have a bunch of dense layers, for making the final prediction. These **dense layers** are specific to the dataset. In imagenet dataset, we have 1000 different classes. In our problem we predict only 10 classes and many of these classes e.g. t-shirt, they dont't exist in imagenet. So vector representation we have from imagenet is useful, but dense layers are not. So we'll keep convolutional layers, but we'll train new dense layers. This is the idea behind **transfer learning**. 

A model was already trained.  It already has all these convolutional layers. We'll use that and build on top of that. We throw away dense layers from imagenet and have our own dense layers. This way the most difficult part from training that the model learnt can be reused. We are kind of transfering these knwoledge to a new model. This is the idea behind **transfer learning**. We'll se how we can do that with ***keras***.

First we need to read our dataset. For that there is a special class claeed `ImageDataGenerator`, that lets us read images from and use them for training.  Run:

```
from tensorflow.keras.preprocessing.image import ImageDataGenerator
```  

