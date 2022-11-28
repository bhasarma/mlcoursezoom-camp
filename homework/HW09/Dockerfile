FROM svizor42/zoomcamp-dino-dragon-lambda:v2

RUN pip install keras-image-helper
RUN pip install --extra-index-url \
	https://google-coral.github.io/py-repo/ tflite_runtime
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl


COPY homework09.py .

CMD ["homework09.lambda_handler"]
