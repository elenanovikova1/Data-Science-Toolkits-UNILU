# Image of tensorflow developers 
FROM tensorflow/tensorflow:2.14.0

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY load_and_prepare_data.py .
COPY neuralnet_architecture.py .
COPY neuralnet_training.py . 
COPY prediction.py .


RUN pip install -r requirements.txt

CMD python main.py
