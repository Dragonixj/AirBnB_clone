#!/usr/bin/python3
"""Contains the main entry point of the command interpreter"""
import cmd

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The class that implements the console
    for the AirBnB project"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Handles the End Of File signal"""
        print()
        return True

    def do_quit(self, line):
        """Exists the console"""
        return True

    def emptyline(self):
        """Doesn't do anything: an empty line + ENTER"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it
        to a JSON file"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(" ")
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = f"{format(words[0])}.{words[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """deletes an instance based on the class name and id"""

        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(" ")
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = f"{format(words[0])}.{words[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all the string representation of all instances"""
        if line != "":
            words = line.split(" ")
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                num_l = [
                    str(obj)
                    for key, obj in storage.all().items()
                    if type(obj).__name__ == words[0]
                ]
                print(num_l)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
