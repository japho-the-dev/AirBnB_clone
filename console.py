#!/usr/bin/python3
""" Command-line interface to the data
elements in the application.
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Entry class to the program."""

    prompt = "(hbnb) "
    missing_class = "** class name missing **"
    missing_id = "** instance id missing **"
    missing_attr = "** attribute name missing **"
    missing_val = "** value missing **"
    unknown_class = "** class doesn't exist **"
    unknown_id = "** no instance found **"

    def emptyline(self):
        """ emptyline """
        pass

    def do_quit(self, args):
        """ Quit cmd - exit the program
        """
        return True

    def do_EOF(self, args):
        """ Aborts the program with EOF cmd
        """
        print()
        return True

    def do_create(self, args):
        """ Module to create a new class,
        saves info and output
        """
        if args == "" or args is None:
            print(self.missing_class)
        else:
            commands = args.split(" ")

            c_name = self.extract_arg(commands[0])
            if c_name in storage.classes():
                new_C= storage.class_map()[c_name]()
                new_C.save()
                print(new_C.id)
            else:
                print(self.unknown_class)

    def do_all(self, args):
        """ Prints all string representation of all instances."""
        if args == "":

            in_list = []
            for _, values in storage.all().items():
                in_list.append(str(values))
                print(in_list)
        else:
            cmd = self.extract_arg(args.split(" ")[0])

            if cmd not in storage.classes():
                print(self.unknown_class)
            else:
                in_list = []
                for _, values in storage.all().items():
                    if type(values).__name__ == cmd:
                        in_list.append(str(values))
                print(in_list)

    def do_show(self, args):
        """ Outputs the str representation
        of a class
        """
        if args == "" or args is None:
            print(self.missing_class)
        else:
            cmds = args.split(" ")
            c_name = self.extract_arg(cmds[0])

            if len(cmds) < 2:
                print(self.missing_id)
            elif c_name not in storage.classes():
                print(self.unknown_class)
            else:
                c_id = self.extract_arg(cmds[1])
                val = "{}.{}".format(c_name, c_id)

                if val in storage.all():
                    print(storage.all()[val])
                else:
                    print(self.unknown_id)

    def do_destroy(self, args):
        """ Removes an entry based
        on class name and id
        """
        if args == "" or args is None:
            print(self.missing_class)
        else:
            cmds = args.split(" ")
            c_name = self.extract_arg(cmds[0])
            c_id = self.extract_arg(cmds[1])

            if len(cmds) < 2:
                print(self.missing_id)
            elif c_name not in storage.class_map():
                print(self.unknown_class)
            else:
                key = "{}.{}".format(c_name, c_id)

                if key in storage.all():
                    storage.all().pop(key)
                else:
                    print(self.unknown_id)


    def do_update(self, args):
        """Updates an instance by adding or updating attribute.
        """
        if args == "" or args is None:
            print(self.missing_class)
        else:
            flags = args.split(" ")
            n_key = "{}.{}".format(self.extract_arg(flags[0]),
                                        self.extract_arg(flags[1]))
            print(n_key)

            if len(flags) < 2:
                print(self.missing_id)
            elif n_key not in storage.all():
                print(self.unknown_id)
            elif len(flags) < 3:
                print(self.missing_attr)
            elif len(flags) < 4:
                print(self.missing_val)
            elif flags[0] not in storage.class_map():
                print(self.unknown_class)

            for key, _ in storage.all().items():
                if n_key == key:
                    setattr(storage.all()[key], flags[2], flags[3])
                    storage.all()[key].save()

    def do_count(self, line):
        """Retuurnc count of attributes in a class.
        """
        characters = line.split(' ')
        if not characters[0]:
            print("** class name missing **")
        elif characters[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            equiv = [
                x for x in storage.all() if x.startswith(
                    characters[0] + '.')]
            print(len(equiv))

    def extract_arg(self, arg="", msg=""):

        if '"' in arg or '\'' in arg:
            return arg[1:-1]
        else:
            return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
