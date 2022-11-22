In this lesson, we'll talk about **data augmentation** i.e  creating data from existing data. 

In the previous lesson we talked about **dropout**, which is a way of **regularizing** our **neural network**. The problem here was that, if our network goes through images many times, it learns from small features e.g. a logo and predict if a logo is there, it is a t-shirt, which is not necessarily true. We talked about dropout as a way to solve this. Its like hiding a part of the image from neural network everytime it sees it. There is a different way of addressing this problem. In case of droupout, we'll freeze a part of network during training. Our different approach this time involves generating more data from existing ones. 

Let's say we take our image. From this image we generate 10 more different images. Then NN will not see exactly the same image every time. 

There are many many different ways that we can use to generate more images from existing ones. There are simple image transformations that we can use to generate more data. First of all, we have the image and we want to generate more pictures from it. One simple thing we can do is:

- we can take this image and flip it (may be horizontal or vertical mirror image).

We have some code for generating these transformations. In keras there is this image data geerator. This image data generator can generate these augmentations. There is some code for doing this. Look at `07-augmentations.ipynb` in [https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/chapter-07-neural-nets](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/chapter-07-neural-nets). 

- Next transformation is **rotation** of the image
- 3rd transformation is **shifting**. We can shift horizontally and vertically. 
- 4th transformation is **shear**. We pull one side down, while other side stays same as before. 
- then zoomin and zoomout, only along x direction or along y-direction
There are also other things we can do. We can play with **brightness** and **contrast**.

- putting a black patch on the image like we discussed in dropout, (although dropout doesn't really do it) is also a way of doing data augmentation. I don't know if keras can do this out-of-the-box, but there are libraries that have this way of data augmentation.

And, there are many other data augmentation techniques. What is more, we can take all this and combine them. They are all combinable at the same time. 

### Choosing augmentation parameter

  - we can do it on our own judgement
  - Look at the images, what kind of variations are there? Are the objects always centred. Depending on that use rotate or shift.
  
  Last thing to remember is: augmentation is also a hyperpaameter of our model. Often we need to try different augmentation and see what works and what doesn't. 
  - tune it as a hyperparameter. It is same as should we use one layer or not, should we use dropout or not and then should we use rotation or not. Then you just take your dataset, add rotation, train for multiple epochs and compare with the same model, but without rotation. See if your score on validation improves or not. 
  
  What I do, train it for 10-20 epochs and see if score is better than without this particular augmentation or not. If it is better, use it. If NO, then don't use it. If it is the same, then train for 20 more epochs, then don't use it. 
  
 **Important:** We do augmentation only on train data. 

