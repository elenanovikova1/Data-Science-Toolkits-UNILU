# Milestone 02

## Task 1

## Task 2

### What is a Hash Function?

A hash function is a mathematical algorithm that, given an input, produces a fixed-size string. These functions are primarily used for security purposes, such as integrity validation and digital signatures. One example of a hash function is SHA-256 (Secure Hash Algorithm 256-bit, to be used in the milestone), which generates an alphanumeric string of 256 bits.

#### Example:

**Input:** "This is an example"  
**Output:** `a1595c7ce2ce119b98bf3b3d9cd4dba9c7d03791af727c76c0e020fc3ea94cfc`

#### Main Characteristics of Hash Functions:

1. **Fixed Size:** The output is of a fixed size. For instance, SHA-256 always produces a 256-bit output, regardless of the input length. But the input should not be longer than 256 bit. 

2. **Deterministic:** The same input always generates the same output hash value.

3. **Irreversibility:** It is computationally infeasible to reverse an output hash value back to the input. Hash functions work only in the direction of input to output.

4. **Collision-Free:** Different inputs result in different outputs. Although collisions (two different inputs producing the same output) are theoretically possible, the probability is extremely low.

5. **Avalanche Effect:** Even a minor change in the input leads to a significant and unpredictable change in the output.

### What is a Python Module, Package, and Script? How Do They Differ from One Another?

#### Script:

A script is a standalone Python file (`.py`) that is directly executable. It consists of Python statements and instructions for performing specific tasks or operations.

**Key Features:**
- Executable file with a sequence of Python code.
- Runs directly using the Python interpreter.

#### Module:

A module is a `.py` file meant to be imported by other scripts or modules. It contains functions, classes, and variables that can be utilized by the importing script or module.

**Key Features:**
- Meant to be reused by importing it into other scripts or modules.
- Organizes code within a single file.
- Enhances code modularity and reusability.

#### Package:

Packages are sets of related modules. These modules work together and are stored in a common folder. A package typically includes an `__init__.py` file, signaling to Python that it is a package and specifying where the modules are stored.

**Key Features:**
- Organizes multiple related modules in a directory. 
- Improves organization of different modules. 

**Hierarchy of Script-Module-Package:**

- A script is a standalone executable file.
- Modules are individual files containing functions, classes and variables to be imported by scripts or other modules. 
- Packages are directories containing related modules, forming a structured and modular organization for related tasks.

### How would you explain a Docker container and volume to a child? 

Docker Container and Volumes: 

Consider this scenario: you and your friend both want to run software on your respective laptops, but there's a challenge – you have a Windows laptop, and your friend has an Apple laptop, with significantly different settings. This is where Docker containers and volumes can help. 

When creating new software, it might work perfectly well on your laptop but not on that of your friend. 

Docker containers are like closed boxes. They not only hold the software itself but also all the necessary information and settings for the software to run on different laptops (e.g. Apple and Windows). Because all the information needed is in the container, the software can run without problem in the container on different computers. 

Now, sometimes the software needs access to data stored on your computer. Then you need volumes. One can imagine volumes like holes in the container, allowing the software to access data that is stored outside of the container. Without volumes (holes), containers could not access any data that is stored outside of this box (container). 

### What is your preference concerning the use of Python virtualenv and Docker? When would you use one
or the other?

For professional software projects, Docker is preferable to virtual environments because it automates the installation of dependencies and ensures the correct Python version. In contrast, with virtual environments, these steps must be repeated each time the software is run on a new computer where the same virtual environment is not yet set up. Virtual environments are also less resilient to mistakes, requiring careful checking and manual installation of dependencies.

With Docker, dependencies are precisely defined and automatically installed with the container image, streamlining the setup process.

Especially in a collaborative environment, where different developers are involved, the correct dependencies management and the consistency of the environment can be ensured by Docker. 

Virtual environments (venvs) could be preferred in quick trials or lightweight projects that don't necessitate running on different systems or adapting dependencies in the future. 

### What is the Docker build context?

The Docker build context is the folder that contains all the necessary files required to build a Docker image. This typically includes essential files such as:

.py (script)
requirements.txt (dependencies)
Data.csv (data that the script utilizes)

When you initiate the Docker build process, Docker uses the contents of this specified folder as the foundation for creating the Docker image. 
The files within the build context are referenced in your Dockerfile, telling Docker on what to include in the image. The build context includes all the relevant components needed to successfully construct the Docker image. The COPY command in your Dockerfile is then used to copy files from the build context into the image.

### How can you assess the quality of a python package on PyPI?

PyPI is an open platform, anyone can publish packages on PyPI and there is no central quality assessment. Therefore a package could also be malicious or contain a virus. 

Therefore it makes sense to take a little bit of research to ensure quality and trustability of the package and its developers. Quality checks could include:

- Check if the package has a clear and consistent documentation 
- Version history of package
- Community ratings, comments on stack overflow
- Community involvement on the respective Git Hub repository 

But also simple indicators like stars and forks on PyPI can be an indicator. If there is very low community involvement, the package might not be secure. 



# Task 2 