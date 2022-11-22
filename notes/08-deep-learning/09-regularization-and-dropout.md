In this lesson, we'll talk about **regularization** and **dropout** as one of the possible ways for reglarizing our neural network. 

Imagine we have an image, that we want to classify as t-shirt. There we see that there is this area with circle and a logo inside it. If we train our model for 10 epochs, it means that we'll go over our dataset 10 times and our neural network will see this image 10 times. When the NN see this so many times, it may recognize a pattern that every time it see a logo like this, it must be a t-shirt. This is not a good rule, because may be we have a cap with a logo in it. Thus shapes such as neck, arm are more important than specific details. Let's see how we can fight this. 

What if we take an image and before NN sees it, we hide a part of the image. Each time NN sees the image, it sees a slightly different version of the image. This is the main idea behind dropout. In **dropout**, we t
randomly hide a part of the input. 

We'll see how dropout works. It is important to remark that: dropout doesn't really hide part of an image, but it applies this idea to immer layers. 



Conclusion:
Here we freezed a part of network in order to not let it overfit.  

Next lesson, we'll do a different approach to regularization. A way of gnerating more data from existing data. 