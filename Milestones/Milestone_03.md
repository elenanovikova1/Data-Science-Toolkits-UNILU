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
--name postgres-db -> runs the container named postgres-db

-p 5432:5432 -> maps the port 5432 of the host machine to the port 5432 of the container

-e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -> sets the environmental variables for the password and the name of the database 

-d postgres:alpine -> runs the container from the image postgres:alpine in detached mode (in the background)

