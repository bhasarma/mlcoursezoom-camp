# 10.2 TensorFlow Serving

In this session, we'll talk about tensorflow serving. In last session, we talked about overview of this module. There we had one component called **TF-serving**, the tool from tensorflow that can be used for serving model. For this, we first have to convert the model, that we trained previously with keras into a special format called `save_model`. 

We'll do this step right now. 

First get the model with `wget`:
```bash
(base) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ wget https://github.com/alexeygrigorev/mlbookcamp-code/releases/download/chapter7-model/xception_v4_large_08_0.894.h5 -O clothing-model-v4.h5
```
Now we need to convert this model saved in `.h5` format into `save_model` format. Let's write a simple code for that. We can also run it line by line in `ipython`.

```python
#saved_model.py
import tensorflow as tf
from tensorflow import keras

#load the model
model = keras.models.load_model('./clothing-model-v4.h5')

#save the model
tf.saved_model.save(model, 'clothing-model')
```

run it from terminal with:
```bash
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ python saved-model.py
```
Content of the folder `clothing-model`:

```bash
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ tree clothing-model
clothing-model
├── assets
├── saved_model.pb
└── variables
    ├── variables.data-00000-of-00001
    └── variables.index

2 directories, 3 files
```
```bash
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ ls -lhR clothing-model
clothing-model:
total 3.5M
drwxr-xr-x 2 bsarma bsarma 4.0K Nov 30 15:26 assets
-rw-rw-r-- 1 bsarma bsarma 3.5M Nov 30 15:26 saved_model.pb
drwxr-xr-x 2 bsarma bsarma 4.0K Nov 30 15:26 variables

clothing-model/assets:
total 0

clothing-model/variables:
total 83M
-rw-rw-r-- 1 bsarma bsarma 83M Nov 30 15:26 variables.data-00000-of-00001
-rw-rw-r-- 1 bsarma bsarma 15K Nov 30 15:26 variables.index
```

Now we can look at what is inside this model using an utility called `saved_model_cli`. This utility comes with tensorflow when we do pip install tensorflow. It will show some information, that we'll later need.

```bash
(ml-zoomcamp) bsarma@turing:~/GitHub/mlcoursezoom-camp/WK13-kubernetes-and-tensorflow-serving$ saved_model_cli show --dir clothing-model --all 

MetaGraphDef with tag-set: 'serve' contains the following SignatureDefs:

signature_def['__saved_model_init_op']:
  The given SavedModel SignatureDef contains the following input(s):
  The given SavedModel SignatureDef contains the following output(s):
    outputs['__saved_model_init_op'] tensor_info:
        dtype: DT_INVALID
        shape: unknown_rank
        name: NoOp
  Method name is: 

signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['input_8'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 299, 299, 3)
        name: serving_default_input_8:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['dense_7'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: StatefulPartitionedCall:0
  Method name is: tensorflow/serving/predict

Defined Functions:
  Function Name: '__call__'
    Option #1
      Callable with:
        Argument #1
          input_8: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_8')
        Argument #2
          DType: bool
          Value: False
        Argument #3
          DType: NoneType
          Value: None
    Option #2
      Callable with:
        Argument #1
          inputs: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='inputs')
        Argument #2
          DType: bool
          Value: False
        Argument #3
          DType: NoneType
          Value: None
    Option #3
      Callable with:
        Argument #1
          input_8: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_8')
        Argument #2
          DType: bool
          Value: True
        Argument #3
          DType: NoneType
          Value: None
    Option #4
      Callable with:
        Argument #1
          inputs: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='inputs')
        Argument #2
          DType: bool
          Value: True
        Argument #3
          DType: NoneType
          Value: None

  Function Name: '_default_save_signature'
    Option #1
      Callable with:
        Argument #1
          input_8: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_8')

  Function Name: 'call_and_return_all_conditional_losses'
    Option #1
      Callable with:
        Argument #1
          inputs: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='inputs')
        Argument #2
          DType: bool
          Value: True
        Argument #3
          DType: NoneType
          Value: None
    Option #2
      Callable with:
        Argument #1
          inputs: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='inputs')
        Argument #2
          DType: bool
          Value: False
        Argument #3
          DType: NoneType
          Value: None
    Option #3
      Callable with:
        Argument #1
          input_8: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_8')
        Argument #2
          DType: bool
          Value: True
        Argument #3
          DType: NoneType
          Value: None
    Option #4
      Callable with:
        Argument #1
          input_8: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_8')
        Argument #2
          DType: bool
          Value: False
        Argument #3
          DType: NoneType
          Value: None
```

We are particularly interested in the `signature_def` part. There are two of them. We don't need the first one. We only need the second one. Let's save the second part in another text file `model-description.txt`

```txt
signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['input_8'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 299, 299, 3)
        name: serving_default_input_8:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['dense_7'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: StatefulPartitionedCall:0
  Method name is: tensorflow/serving/predict
``` 

This `signature_def` is something technical, but we need to know these input and output values for what kind of signature we need to invoke. This data will be used later when we invoke our model. 

Now we can use tensorflow-serving locally using this model. 

```bash
docker run -it --rm -p 8500:8500 -v "$(pwd)/clothing-model:/models/clothing-model/1" -e MODEL_NAME="clothing-model" tensorflow/serving:2.7.0
```

Now let's try to send something to this model.



**References:**
1. [ML Zoomcamp 10.2 - TensorFlow Serving](https://www.youtube.com/watch?v=deXR2fThYDw&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=99)