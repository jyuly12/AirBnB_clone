#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """
import cmd
import sys
from models import storage
# modifiable objects from the console
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Defines command interpreter parameters
    """
    prompt = '(hbnb) '
    classes = ['Amenity', 'BaseModel', 'City',
               'Place', 'Review', 'State', 'User']

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self, arg):
        pass

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id.
        """
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] in self.classes:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        key = '{}.{}'.format(args[0], args[1])
        objects = storage.all()
        if key in objects.keys():
            print(objects[key])
        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        key = '{}.{}'.format(args[0], args[1])
        objects = storage.all()
        if key in objects.keys():
            # 1. update __objects
            objects.pop(key)
            # 2. serialize and save objects
            storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name.
        """
        args = arg.split()
        list_of_strings = []
        objects = storage.all()
        for key in objects.keys():
            value = objects.get(key)
            if args:
                # if they asked us for objects of a certain class
                if args[0] in self.classes:
                    # if we create that kind of objects
                    if value.__class__.__name__ == args[0]:
                        # if the class of the object matches
                        # the one they ask us
                        list_of_strings.append(value.__str__())
                else:
                    print("** class doesn't exist **")
                    return
            else:
                list_of_strings.append(objects[key].__str__())
        print(list_of_strings)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            object_name = '{}.{}'.format(args[0], args[1])
            dict_of_objects = storage.all()
            if object_name in dict_of_objects.keys():
                object = dict_of_objects.get(object_name)
                object.__setattr__(args[2], args[3][1:-1])
                storage.save()
            else:
                print("** no instance found **")
                return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
