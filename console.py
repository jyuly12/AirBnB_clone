#!/usr/bin/python3
'''  This module contains the entry point of the command interpreter: '''
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    '''  '''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        sys.exit(0)

    def emptyline(self, arg):
        pass

    def do_EOF(self, arg):
        '''
        Quit command to exit the program
        '''
        sys.exit(0)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
