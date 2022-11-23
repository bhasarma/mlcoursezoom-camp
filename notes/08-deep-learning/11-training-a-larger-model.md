In this lesson we'll train a larger model. Till now we have been doing it with images of size 150x150. Now we'll train a 299x299 image. 150x150 models train 4x faster than 299x299. We wanted to iterate quicker and experiment with different parameters. But now its time to train a larger model. 

In the book we trained the final model with augmentattion. We should do it as well. 

We shouldn't forget about checkpointing. 

xception_v1: transferrred learning with just one dense layer
xception_v2: with inner dense layer
xception_v3: added dropout
xception_v4: just model from v3, but bigger.