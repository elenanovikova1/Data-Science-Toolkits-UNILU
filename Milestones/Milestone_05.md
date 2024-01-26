#Milestone 5 Task 1

We successfully went through a [Flask tutorial](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04). 
This tutorial covers the essentials of using Docker and Flask. To complete the task (task 2) we also had to use additional materials we found in the internet (e.g. replies from stackoverflow).


#Milestone 5 Task 2

Please note that the 'docker-compose.yml' is in the folder 'Milestone 5' (Please run `docker-compose up` from there).
Due to an issue with the *blinker* package, we decided to create venv using the Dockerfile. Another option would have been to use the `--ignore-installed` flag, that is, to have

```
RUN pip install --no-cache-dir --ignore-installed -r requirements.txt
```

in the Dockerfile. However, we were not sure whether it does not create problems, since versions of the packages might be important, so we decided to use venv instead.
It affects the time of the first usage of `docker-compose up` (can be up to **5 minutes**). Next usages of `docker-compose up` are of course not affected and are performed fast.

The Flask application exposes a REST API endpoint `/predict`, which processes incoming POST requests. The requests include base64-encoded images, which are decoded, resized, and normalized before being fed into the model. The prediction is returned to the caller, and the code of the image and the prediction are saved in a database (we tested it and it worked as expected).

The Flask app code ('app.py') is in the folder 'flask' (a direct subfolder of 'Milestone 5'). There are also two other python files in this sub-folder: 'database\_utils.py' and 'image\_binary\_convertation.py'. They are similar to the files we had in Milestone 3, but have some minor differences in implementation (e.g. we removed a boolean parameter that indicated that an image is from the test or from the train sample). In addition, we store the model in the file 'saved\_model.keras' (also in the 'flask' subfolder).

For our app it is important that the image is encoded into a string via base64. Here is an example of the code that takes an image from the file whose path is stored in a variable `image_file_name`:

```
with open(image_file_name, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

data = {"image": encoded_string}

url = "http://localhost:5001/predict"

response = requests.post(url, json=data)

print(response.json())
```
We used a file 'test.py' (and an image 'image0.png') to test the app (the code above is a fragment of 'test.py').

5001 in the code above is the number of the port that we use. We remark that port 5000 was not available on Elena's machine, so we had to use

```
ports:

  - "5001:5000"
```

in the 'docker-compose.yml' (it maps port 5001 on your host to port 5000 in the container).

The parameters of the database are as follows:

```
host = 'db'
port = 5432
user = 'postgres'
password = 'mypassword'
database = 'milestone_5'
table_name = 'mnist_table'
```
