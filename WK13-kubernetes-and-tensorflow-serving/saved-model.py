import tensorflow as tf
from tensorflow import keras

#load the model
model = keras.models.load_model('./clothing-model-v4.h5')

#save the model
tf.saved_model.save(model, 'clothing-model')
