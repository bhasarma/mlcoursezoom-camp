#!/usr/bin/env python
# coding: utf-8


#import the packages
#import tensorflow.lite as tflite
import tflite_runtime.interpreter as tflite
from io import BytesIO
from urllib import request
from PIL import Image
import numpy as np
#from tensorflow.keras.preprocessing.image import ImageDataGenerator


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



#uncomment below line for question 1-5
#interpreter = tflite.Interpreter(model_path='dino-or-dragon.tflite')
#for question 6
interpreter = tflite.Interpreter(model_path='dino-vs-dragon-v2.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

#url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px-Smaug_par_David_Demaret.jpg'
#function for prediction
def predict(url):    
    image = download_image(url)

    image = prepare_image(image, target_size=(150,150))
    
    x = np.array(image, dtype='float32')
    X = np.array([x])
    X = X*(1./255)

    interpreter.set_tensor(input_index,X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    return float(preds[0, 0])


def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {'prediction': pred}
    return result