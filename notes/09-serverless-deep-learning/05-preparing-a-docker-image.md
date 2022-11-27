## 9.5 Preparing a Docker Image

In this session, we'll prepae a docker image for publishing it to AWS Lambda. In the previous session, we took the notebook we had and convetred this notebook to a python script. We tested this python script locally. We  saw that it works. Now we want to package everything inside a docker container. 

For the base image, we will use the image preparared by AWS. Go to `https://gallery.ecr.aws/`. These are public images created by AWS. Then let's look for Lambda. 


After writing Dockerfile, we build it with:

```
docker build -t clothing-model .
```

I got in CLI:

```bash

Sending build context to Docker daemon  170.8MB
Step 1/6 : FROM public.ecr.aws/lambda/python:3.9
3.9: Pulling from lambda/python
625fcf1e5e5f: Pull complete 
9816edaa7ba6: Pull complete 
b90d26e93f3d: Pull complete 
94130148b8a0: Pull complete 
4bdeb01d286b: Pull complete 
9c8d9df1252e: Pull complete 
Digest: sha256:b151438a56896f7fe83c0ba6880fd1f5a1db6040babff9dd779d3b6b30043dae
Status: Downloaded newer image for public.ecr.aws/lambda/python:3.9
 ---> 7facc9194ea7
Step 2/6 : RUN pip install keras-image-helper
 ---> Running in b919a5dfc8c1
Collecting keras-image-helper
  Downloading keras_image_helper-0.0.1-py3-none-any.whl (4.6 kB)
Collecting numpy
  Downloading numpy-1.23.5-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.1/17.1 MB 3.9 MB/s eta 0:00:00
Collecting pillow
  Downloading Pillow-9.3.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 4.5 MB/s eta 0:00:00
Installing collected packages: pillow, numpy, keras-image-helper
Successfully installed keras-image-helper-0.0.1 numpy-1.23.5 pillow-9.3.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
You should consider upgrading via the '/var/lang/bin/python3.9 -m pip install --upgrade pip' command.
Removing intermediate container b919a5dfc8c1
 ---> 7b2524ffb291
Step 3/6 : RUN pip install --extra-index-url 	https://google-coral.github.io/py-repo/ tflite_runtime
 ---> Running in b06020f3fc7e
Looking in indexes: https://pypi.org/simple, https://google-coral.github.io/py-repo/
Collecting tflite_runtime
  Downloading tflite_runtime-2.10.0-cp39-cp39-manylinux2014_x86_64.whl (2.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 3.0 MB/s eta 0:00:00
Requirement already satisfied: numpy>=1.19.2 in /var/lang/lib/python3.9/site-packages (from tflite_runtime) (1.23.5)
Installing collected packages: tflite_runtime
Successfully installed tflite_runtime-2.10.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
You should consider upgrading via the '/var/lang/bin/python3.9 -m pip install --upgrade pip' command.
Removing intermediate container b06020f3fc7e
 ---> 221ea9157eb7
Step 4/6 : COPY clothing-model.tflite .
 ---> 0c73ac1de252
Step 5/6 : COPY lambda_function.py .
 ---> dc0b2b8d8484
Step 6/6 : CMD ["lambda_function.lambda_handler"]
 ---> Running in ec850a9a161a
Removing intermediate container ec850a9a161a
 ---> 126d89cb31b0
Successfully built 126d89cb31b0
Successfully tagged clothing-model:latest

```

Then run the docker image through:

```
docker run -it --rm -p 8080:8080 clothing-model:latest
```
Now lets test it with a new file `test.py`