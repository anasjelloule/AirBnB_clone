#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
import ast
from models.base_model import BaseModel
from models.user import User
from models import storage
from shlex import split
import shlex
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {"BaseModel",
               "User", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    do_EOF = do_quit

    def do_create(self, line):
        """creates an object"""
        if not len(line):
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        nwObj = eval(line)()
        print(nwObj.id)
        nwObj.save()

    def do_show(self, line):
        """shows an object"""
        if not len(line):
            print("** class name missing **")
            return
        strs = split(line)
        if strs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strs) == 1:
            print("** instance id missing **")
            return
        K_V = strs[0] + '.' + strs[1]
        if K_V not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[K_V])

    def do_destroy(self, line):
        """deletes an object"""
        if not len(line):
            print("** class name missing **")
            return
        strs = split(line)
        if strs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strs) == 1:
            print("** instance id missing **")
            return
        K_V = strs[0] + '.' + strs[1]
        if K_V not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[K_V]
        storage.save()

    def do_all(self, line):
        """prints all"""
        if not len(line):
            print([obj for obj in storage.all().values()])
            return
        strs = split(line)
        if strs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([obj for obj in storage.all().values()
               if strs[0] == type(obj).__name__])

    def do_update(self, line):
        """updates an object"""
        if not len(line):
            print("** class name missing **")
            return
        strs = split(line)
        for string in strs:
            if string.startswith('"') and string.endswith('"'):
                string = string[1:-1]
        if strs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strs) == 1:
            print("** instance id missing **")
            return
        K_V = strs[0] + '.' + strs[1]
        if K_V not in storage.all().keys():
            print("** no instance found **")
            return
        if len(strs) == 2:
            print("** attribute name missing **")
            return
        if len(strs) == 3:
            print("** value missing **")
            return
        try:
            setattr(storage.all()[K_V], strs[2], eval(strs[3]))
        except:
            setattr(storage.all()[K_V], strs[2], strs[3])

    def emptyline(self):
        """passes"""
        pass

    def stripper(self, st):
        """strips that line"""
        nwstr = st[st.find("(")+1:st.rfind(")")]
        nwstr = shlex.shlex(nwstr, posix=True)
        nwstr.whitespace += ','
        nwstr.whitespace_split = True
        return list(nwstr)

    def dict_strip(self, st):
        """tries to find a dict while stripping"""
        nwstr = st[st.find("(")+1:st.rfind(")")]
        try:
            nwdict = nwstr[nwstr.find("{")+1:nwstr.rfind("}")]
            return eval("{" + nwdict + "}")
        except:
            return None

    def default(self, line):
        """defaults"""
        su_args = self.stripper(line)
        strs = list(shlex.shlex(line, posix=True))
        if strs[0] not in HBNBCommand.classes:
            print("*** Unknown syntax: {}".format(line))
            return
        if strs[2] == "all":
            self.do_all(strs[0])
        elif strs[2] == "count":
            cnt = 0
            for obj in storage.all().values():
                if strs[0] == type(obj).__name__:
                    cnt += 1
            print(cnt)
            return
        elif strs[2] == "show":
            key = strs[0] + " " + su_args[0]
            self.do_show(key)
        elif strs[2] == "destroy":
            key = strs[0] + " " + su_args[0]
            self.do_destroy(key)
        elif strs[2] == "update":
            nwdict = self.dict_strip(line)
            if type(nwdict) is dict:
                for key, val in nwdict.items():
                    ky_V = strs[0] + " " + su_args[0]
                    self.do_update(ky_V + ' "{}" "{}"'.format(key, val))
            else:
                key = strs[0]
                for arg in su_args:
                    key = key + " " + '"{}"'.format(arg)
                self.do_update(key)
        else:
            print("*** Unknown syntax: {}".format(line))
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
