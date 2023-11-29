# Milestone 02

## Task 1: 

###What is a Hash Function?

A hash function is a mathematical operation that, given an input, produces a fixed-size string. These functions are primarily used for security purposes, such as integrity validation and digital signatures. One example of a hash function is SHA-256 (Secure Hash Algorithm 256-bit), which generates an alphanumeric string of 256 bits.

#### Example:

**Input:** "This is an example"  
**Output:** `a1595c7ce2ce119b98bf3b3d9cd4dba9c7d03791af727c76c0e020fc3ea94cfc`

#### Main Characteristics of Hash Functions:

1. **Fixed Size:** The output is of a fixed size. For instance, SHA-256 always produces a 256-bit output, regardless of the input length.

2. **Deterministic:** The same input always generates the same output hash value.

3. **Irreversibility:** It is computationally infeasible to reverse an output hash value back to the input. Hash functions work only in the direction of input to output.

4. **Collision-Free:** Different inputs result in different outputs. Although collisions (two different inputs producing the same output) are theoretically possible, the probability is extremely low.

5. **Avalanche Effect:** Even a minor change in the input leads to a significant and unpredictable change in the output.

## What is a Python Module, Package, and Script? How Do They Differ from One Another?

### Script:

A script is a standalone Python file (`.py`) that is directly executable. It consists of Python statements and instructions for performing specific tasks or operations.

**Key Features:**
- Executable file with a sequence of Python code.
- Runs directly using the Python interpreter.

### Module:

A module is a `.py` file meant to be imported by other scripts or modules. It contains functions, classes, and variables that can be utilized by the importing script or module.

**Key Features:**
- Meant to be reused by importing it into other scripts or modules.
- Organizes code within a single file.
- Enhances code modularity and reusability.

### Package:

Packages are directories that contain different related modules. These modules work together and are stored in a common folder. A package typically includes an `__init__.py` file, signaling to Python that it is a package and specifying where the modules are stored.

**Key Features:**
- Organizes multiple related modules in a directory. 
- Improves organization of different modules. 

**Hierarchy of Script-Module-Package:**

- A script is a standalone executable file.
- Modules are individual files containing functions, classes and variables to be imported by scripts or other modules. 
- Packages are directories containing related modules, forming a structured and modular organization for related tasks.

## How would you explain a Docker container and volume to a child? 



# Task 2 