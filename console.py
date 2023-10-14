#!/usr/bin/python3
"""Contains the main entry point of the command interpreter"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """The class that implements the console
    for the AirBnB project"""

    prompt = "(hbnb)"
    storage = models.storage

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
