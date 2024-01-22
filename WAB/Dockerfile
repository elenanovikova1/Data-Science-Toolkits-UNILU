# Image of tensorflow developers 
FROM tensorflow/tensorflow:2.14.0

WORKDIR /app


COPY main_wab.py .
COPY load_and_prepare_data.py .
COPY neuralnet_architecture.py .
COPY neuralnet_training.py .
COPY prediction.py .


RUN pip install -r requirements.txt

# Set the entrypoint script as executable
RUN chmod +x entrypoint.sh

# Set the entrypoint for running the script
ENTRYPOINT ["./entrypoint.sh"]

CMD python main_wab.py
