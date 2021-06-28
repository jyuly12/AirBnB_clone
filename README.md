# AirBnB clone - console
Welcome to our AirBnB console proyect.

> ## Synopsis

This is the starting point of a series of projects that create a copy of AirBnB, this project focuses on creating a command interpreter, in addition to executing the process of storage and persist objects to a `file.json`

Unlike the shell, our command interpreter is limited to a single use-case (managing the objects of our project), so it must be able to:
-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

--------------------------

> ## Requirements

### Python Scripts
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3`  (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `PEP 8`  style (version 1.7 or more)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
----
### Python Unit Tests
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder  `tests`
-   You have to use the unittest module
-   All your test files should be python files (extension:  `.py`)
-   All your test files and folders should start by  `test_`
-   Your file organization in the tests folder should be the same as your project
-   e.g., For  `models/base_model.py`, unit tests must be in:  `tests/test_models/test_base_model.py`
-   e.g., For  `models/user.py`, unit tests must be in:  `tests/test_models/test_user.py`
-   All your tests should be executed by using this command:  `python3 -m unittest discover tests`
-   You can also test file by file by using this command:  `python3 -m unittest tests/test_models/test_base_model.py`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   We strongly encourage you to work together on test cases, so that you don’t miss any edge case
---------------------------------------------------------
>## Content
This repository contains the following files:
- **console.py** : What sets the console settings
-  **models** : This directory contains the files that define the _Amenity_, _BaseModel_, _City_, _Place_, _Review_, _State_ and _User_ classes, which are necessary parameters for the creation of the AirBnB clone.
- **models/engine** : This directory contains the file that defines the _FileStorage_ class that is responsible for storing the data in a .json file
- **tests** : This directory contains the test files run in the repository.
--------------------------------------------------
>## Execution
This command interpreter works in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Or in non-interactive mode:
```
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)


Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$
```
----
### Console commands

The commands implemented in our command interpreter are explained in the following table:
|Command| Description |Usage|
|--|--|--|
|Create| Creates a new instance of `<class_name>`, saves it (to the JSON file) and prints the `id`. | `$ create <class_name>`|
|Show|Prints the string representation of an instance based on the class name and `id`|`$ show <class_name> <class_id>`|
| Destroy | Deletes an instance based on the class name and `id` (save the change into the JSON file) |`$ destroy <class_name> <class_id>`|
|All|Prints all string representation of all instances based or not on the class name.|`$ all <class_name>`|
|Update|Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file).|`$ update <class_name> <class_id> <attribute> <new_value>`|
|quit and EOF|Exit the program| `$ quit`|
|help|Displays the documented commands.|`$ help`, `$ ?`|


Some examples of the use of the commands mentioned in the table.
- **create a new object**
  ```
  (hbnb) create BaseModel
  7e857e75-d8d4-4aee-8d77-42c247cf9696
  ```
- **show a object**
  ```
  (hbnb) create BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696
  [BaseModel] (7e857e75-d8d4-4aee-8d77-42c247cf9696) {'id': '7e857e75-d8d4-4aee-8d77-42c247cf9696', 'created_at': datetime.datetime(2021, 6, 28, 13, 55, 27, 692778), 'updated_at': datetime.datetime(2021, 6, 28, 13, 55, 27, 694050)}
  ```

- **update object attribute**
  ```
  (hbnb) update BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696 name "Betty"
  (hbnb) show BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696
  [BaseModel] (7e857e75-d8d4-4aee-8d77-42c247cf9696) {'id': '7e857e75-d8d4-4aee-8d77-42c247cf9696', 'created_at': datetime.datetime(2021, 6, 28, 13, 55, 27, 692778), 'updated_at': datetime.datetime(2021, 6, 28, 13, 55, 27, 694050), 'name': 'Betty'}
  ```
- **remove object**
  ```
  (hbnb) destroy BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696
  (hbnb) show BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696
  ** no instance found **
  ```
----
>## Testing
The test files are located in the **/tests** directory, to run it you can use the command
` python3 -m unittest discover tests`

---
>## Authors
-  **Julieth Gonzalez** [github](https://github.com/jyuly12)  - [twitter](https://twitter.com/jyuly12)
-  **Natalia Vera**  [github](https://github.com/Naveduran)  -  [twitter](https://twitter.com/NaVeDuran1)
