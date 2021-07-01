# AirBnB clone - console
Welcome to our AirBnB console proyect.

![](https://pbs.twimg.com/media/E5OfUqaX0AIQ-WK?format=jpg&name=small)

> ## Synopsis

This is the starting point of a series of projects that create a copy of AirBnB, this project focuses on creating a command interpreter, in addition to executing the process of storage and persist objects to a `file.json`

Our command interpreter is limited to a single use-case (managing the objects of our project), so it is able of:
-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

---------------------------------------------------------
>## Content
This repository contains the following files:

- **console.py** : Execute this file to open the Console. 
-  **models** : This directory contains the files that define the _Amenity_, _BaseModel_, _City_, _Place_, _Review_, _State_ and _User_ classes for the creation of the AirBnB clone.
- **models/engine** : This directory defines the _FileStorage_ class that is responsible for storing the console's data in a .json file.
- **tests** : This directory contains the unittests.
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
- **Create a new object**
  ```
  (hbnb) create BaseModel
  7e857e75-d8d4-4aee-8d77-42c247cf9696
  ```
- **Show a object**
  ```
  (hbnb) create BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696
  [BaseModel] (7e857e75-d8d4-4aee-8d77-42c247cf9696) {'id': '7e857e75-d8d4-4aee-8d77-42c247cf9696', 'created_at': datetime.datetime(2021, 6, 28, 13, 55, 27, 692778), 'updated_at': datetime.datetime(2021, 6, 28, 13, 55, 27, 694050)}
  ```

- **Update object attribute**
  ```
  (hbnb) update BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696 name "Betty"
  (hbnb) show BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696
  [BaseModel] (7e857e75-d8d4-4aee-8d77-42c247cf9696) {'id': '7e857e75-d8d4-4aee-8d77-42c247cf9696', 'created_at': datetime.datetime(2021, 6, 28, 13, 55, 27, 692778), 'updated_at': datetime.datetime(2021, 6, 28, 13, 55, 27, 694050), 'name': 'Betty'}
  ```
- **Remove object**
  ```
  (hbnb) destroy BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696
  (hbnb) show BaseModel 7e857e75-d8d4-4aee-8d77-42c247cf9696
  ** no instance found **
  ```
----
>## Testing
The test files are located in the **/tests** directory, to run it you can use the command
` python3 -m unittest discover tests`

----
>## Environment
This project has been tested on Ubuntu 14.06.6 LTS

----
>## Version
Released on July 1th of 2021.

---
>## Authors
-  **Julieth Gonzalez** [github](https://github.com/jyuly12)  - [twitter](https://twitter.com/jyuly12)
-  **Natalia Vera**  [github](https://github.com/Naveduran)  -  [twitter](https://twitter.com/NaVeDuran1)
