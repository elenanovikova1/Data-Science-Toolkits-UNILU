FROM python:3.8
FROM tensorflow/tensorflow:2.14.0

WORKDIR /usr/src/app

COPY ../requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY MNIST_Database/ .

# Define the command to run your program
CMD ["python", "./task4.py"]