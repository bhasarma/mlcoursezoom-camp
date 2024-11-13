In this lesson, we'll talk about using a pre-trained convolutional neural network for making prediction. 

In the previous lesson, we talked about TensorFlow ans Keras : how to install them and how to load images. We also talked about how images are represented internally and how to convert images into numpy array. 

Now we'll take this image and use a NN that was already trained by somebody and made it available for us. We can just take it and use it. 

Go to Keras website with pretrained models: [https://keras.io/api/applications/](https://keras.io/api/applications/). It has a list of pretrained available models. Most of these models were trained on [imagenet](https://www.image-net.org/). It is a dataset with lots of images. We can download it. There are 1000 classes (all sorts of animals, objects) and 1.3 miilion images in training dataset, 50k in validation and 100k in test dataset. We don't have to download these huge datasets. Someone in big companies trained these models (in keras applications) and shared results. They are avaliable in keras website. There are different models. We'll not go into details of these images. These are different models with different architectures: how exactly the layers of a NN are arranged inside a model. Based on the characteristics (size, accuracy etc.) of the model listed, we can choose which one we want to use. We'll use the `Xception` model. We can use it following way: 

```
tf.keras.applications.Xception(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
)
```

GPUs are good at paralleizing things. They are good at fast matrix multiplication and number crunching operations. 

Conclusion: we see that this model is particularly not good for our images. Therefore, we need to train our own model. Good news here is that we don't have to retrain our model from scratch. We can build on the top of what has been provided by big companies and universities. 

**References:**<br>
- [https://www.youtube.com/watch?v=qGDXEz-cr6M&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=71]()

***keywords:***<br>
Pretrained Convolutional Neural Network and Xception. 
