# Milestone 03

Add on a table with the SHA256 hashes 

## Task 1

Docker-compose has already been installed on the local machine together with the docker engine. (Version 2.23.0) 

### Which services are being used for the application (described in the link above)? How do they relate to the host names in terms of computer networks?

Two services are being used for the application ```web```: hosting a web application and ```redit```: a NoSQL Database.

Each service is assigned a hostname, a human-readable label. These hostnames are identifiers, simplifying communication between containers within the same network. Using these hostnames allows containers to interact with each other. The services defined in docker-compose (with its hostname) are discoverable by their designated names within the Docker network. 

### What ports are being used (within the application and in the docker-compose file)?

Within docker-compose file: ```ports: - "8000:5000"``` - the port 8000 on the host machine is mapped to the port 5000 inside the container for the web service. 

Within the application: ```cache = redis.Redis(host='redis', port=6379)``` - the port on which the Redis Server is running is 6379

### How does the host machine (e.g. your computer) communicate with the application inside the Docker container. Which ports are exposed from the application to the host machine? ###

See question above, the host machine can communicate with the application inside the Docker container by accessing port 8000.

### What is localhost, why is it useful in the domain of web applications?

The label localhost is referring to the local host machine with the IP address: 127.0.0.1. It allows a computer to connect to itself, and any data sent to localhost is routed back to the local machine.

In general a localhost is suitable in the development phase to simulate interaction with a host without actually connecting with an external server. 

## Task 2

### What is PostgreSQL? Is it SQL or no-SQL (why?)

PostgreSQL is a relational database system and is based on the conventions and rules of a relational SQL databases. Data is stored in tables with predefined relationships. SQL is used as query language. 
Whereas a NoSQL doesn't completely adhere to these principles. 


### Run a PostgreSQL Server (current version is 14.0) using a Docker image from the official PostgreSQL Docker Hub page ###

The following steps have to be executed to run a PostgreSQL server using an image from PostgreSQL. 
Download the current image 14.0: 

```
$ docker pull postgres:14.0
```

Run the container: 
```
$ docker run --name postgres-db -p 5432:5432 -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -d postgres:14.0
```

Lets break this down:
```--name postgres-db```: runs the container named postgres-db

```-p 5432:5432```: maps the port 5432 of the host machine to the port 5432 of the container

```-e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase```: sets the environmental variables for the password and the name of the database 

```-d postgres:14.0```: runs the container from the image postgres:alpine in detached mode (in the background)

### Python app to create database, writes and reads from it and prints the result 


First install the client psycopg2. We had to install the binary version of the client, the psycopgn2 itself didn't work - update requirements.txt with this package 

```
$ pip install psycopg2-binary:2.9.9
```

We created a python script (in folder Database) that connects to the database above ```mydatabase``` on the specified port 5432 with the username and password selected for the postgreSQL server running in the docker container postgres-db. 
The python script ```jokes.py``` creates a table ms3_jokes with the ```id``` and ```jokes``` column. 
The script saves some jokes in the table and script ```read_out.py``` selects one random joke that gets printed out. 

### Download the PGADMIN Tool (https://www.pgadmin.org/download/). It also exists as a Docker Image :). Connect to your running PostgreSQL Database. Can you see your database and table?

First couldn't read out the jokes with a second script that only connects to the database to read out the jokes. We forgot to commit the changes. Added con.commit() after every change in the database - Now it appears in pgAdmin - used the following query ```SELECT * FROM ms3_jokes``` to show all the entries. 

### If you stopped and deleted the Docker container running the database and restarted it. Would your joke still be in the database? Why or why not?

The jokes were still in the database if the container was just stopped and restarted. But the jokes disappeared if the container is deleted. If run again a new instance of the container is created. 

```$ docker stop postgres-db```
```$ docker rm postgres-db```
## Task 3


###  How do you need to represent/transform image data to save it to a relational database?

Binary Data Representation: Images are not inherently structured in a way that fits neatly into relational databases, which are optimized for textual and numerical data. To store images in such a database, you need to convert them into a format that the database can handle. A common approach is to transform images into binary data (BLOB - Binary Large OBject). This involves encoding the image files into a binary format.

### Working with our dataset
####1. How is your data structured?
MNIST Dataset Overview: The MNIST dataset consists of 28x28 pixel grayscale images of handwritten digits (0 through 9). Each pixel can be represented as a number (0-255), where 0 represents black and 255 represents white. More detailed description of the dataset has already been provided in the previous Milestones projects.

####2. Explain how you would define your relational database tables in terms of their attributes to save your data. What kind of data types could you use (https://www.postgresql.org/docs/12/datatype.html)?
Considering the nature of the MNIST dataset, we create a table named "mnist_table" with the following columns:

- id (Data type: SERIAL PRIMARY KEY): a unique identifier for each image
- image_binary (Data type: BYTEA): the binary representation of the image
- label (Data type: INTEGER): the digit that the image represents
- is_train (Data type: BOOLEAN): flag that indicates the data set where the images comes from (True for Train and False for Test)

####3. What additional relational database table attributes might make sense to easily query your data (f.e. find all pictures of giraffes)

TBA

### Task 2 using a sample from your own data set 

Files related to the folution of this point are located in the folder "MNIST_Database":

- task3:
	- it was interesting to have a possibility to insert several images into a database, since there are many images two parameter were used 
```n_train_images = 10```
```n_test_images = 5```
	- Connestion to the server was done the same way as in the previous task with jokes dataset with exception that names were changed 
```database = 'mnist_database'```
```table_name = 'mnist_table'```
	- Block starts with command ```try:``` : code trys to create a table
	- Block starts with command ```except:``` : if an error occurs in ```psycopg2``` then it indicates that the table might already exist, in this case we do not insert anything
	- Block starts with command ```else:``` : the table did not exist, we successfuly create it and insert images
	- Block starts with command ``finally:``` : independantly of whether the table existed or not, we show an image iwth image id, print its label and dataset name where it comes from
- image\_binary\_converation: there are two functions that convers image data from our dataset into binary format and back (from binary to image)
- mnist\_datasabe\_utils: there are multiple functions in this file, incl. creation of the table for database, insertion images data, showing images by id


There are also comments in the code to some sections with explanation what is performed in each section.

## Task 4
TBA

## Additional question
###What is an SQL Injection Attack and how can you protect yourself?