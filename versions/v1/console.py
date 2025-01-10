#!/usr/bin/python3
"""
console module
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.models import User, Program, Course
from models.models import Project, Enrollment, Resource
from models.models import Quiz
from models.models import  UserQuiz
from models import storage



class EduPahtwayommand(cmd.Cmd):
    """Console class"""
    prompt = '(RoofMarket) ' if sys.__stdin__.isatty() else ''
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Program': Program,
               'Course': Course, 'Project': Project, 'Enrollment': Enrollment,
               'Resource': Resource, 'Quiz': Quiz, 'UserQuiz': UserQuiz
              }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_EOF(self, line):
        """Handle End-of-File (EOF) condition to exit the program gracefully"""
        print()
        return True

    def do_create(self, args):
        """ Create an object of any type

            Usage: create class_name
        """
        try:
            for i in range(1):
                arguments = shlex.split(args)
                f_arguments = arguments[1:]
                if not args:
                    print("** class doesn't exist **")
                    return
                elif arguments[0] not in EduPahtwayommand.classes:
                    print("** class doesn't exist **")
                    return
                new_instance = globals()[arguments[0]]()

                for my_args in f_arguments:
                    key, value = my_args.split("=")
                    print(type(key), type(value))
                    setattr(new_instance, key, value)
                new_instance.save()
                print(new_instance.id)
        except Exception as e:
            print(e)


    def do_destroy(self, args):
        """Delete an object or row from the database
        Usage: destroy class_name object_id
        
        """
        
        arguments = shlex.split(args)
        if not args:
            print("** class doesn't exist **")
            return
        elif arguments[0] not in EduPahtwayommand.classes:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 1:
            print("** provide the id of the object **")
            return
        ob_id = "{}.{}".format(arguments[0].lower(), arguments[1])
        for key, value in storage.all(arguments[0]).items():
            if (key == ob_id):
                value.delete()
                storage.save()

    def do_all(self, args):  
        print(storage.get_object(User))

if __name__ == '__main__':
    EduPahtwayommand().cmdloop()
