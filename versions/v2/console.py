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
import time


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
        courses = [
            {
                "name": "Introduction to Game Development",
                "description": "An introduction to game development, focusing on fundamental game design principles, game programming, and building the first simple games.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Game Programming with C++",
                "description": "Learn how to program games using C++. The course will cover C++ basics, object-oriented programming, and techniques used in game development.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Game Design Fundamentals",
                "description": "Introduction to the principles of game design, including how to develop gameplay, story, and character concepts, and how to create a fun and engaging player experience.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "3D Game Development",
                "description": "Learn the fundamentals of 3D game development, including 3D graphics, physics, animation, and object interaction within a game engine.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Introduction to Unity",
                "description": "Learn how to use Unity, one of the most popular game engines, for developing 2D and 3D games. Covers Unity's interface, scripting, and the development workflow.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Game Physics",
                "description": "Learn about the physics systems that drive many of the interactions in modern games, including motion, collision detection, and realistic object behavior.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Artificial Intelligence in Games",
                "description": "Learn how to implement AI techniques in games. This includes creating NPC behaviors, pathfinding, decision trees, and using AI to make gameplay more challenging.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Game Sound Design",
                "description": "Understand the importance of sound in games and how to design immersive soundscapes, sound effects, and music that support gameplay and enhance the player's experience.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Multiplayer Game Development",
                "description": "Explore the challenges and techniques in developing multiplayer games, including networking, client-server architecture, synchronization, and latency issues.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Virtual Reality Game Development",
                "description": "Learn how to create immersive virtual reality (VR) games using Unity and other tools. Understand VR interaction, motion tracking, and VR design principles.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Game Monetization Strategies",
                "description": "Understand how to monetize games, including in-app purchases, advertising, and other business models that generate revenue from your game.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            },
            {
                "name": "Capstone Project in Game Development",
                "description": "Complete a capstone project where students design, develop, and launch a game from concept to release, showcasing all the skills learned in the program.",
                "program_id": "02c94fb2-ca4f-40c4-b1a9-7cae35f76aa1",
                "user_id": "fcff5d35-4d4f-4afa-a0dd-35d399d3884c"
            }
        ]






















        for course in courses:
            # Format the course data into an argument string
            arguments = "Course name='{}' description='{}' program_id='{}' user_id='{}'".format(
                course['name'], course['description'], course['program_id'], course['user_id']
            )
            print(f"Creating course with arguments: {arguments}")
            
            # Split arguments manually ensuring that the description field is handled properly
            try:
                # Use shlex.split to handle quoted strings and spaces properly
                arguments_list = shlex.split(arguments)

                # Ensure that the class exists and arguments are valid
                if not arguments_list:
                    print("** class doesn't exist **")
                    continue  # Skip this iteration
                elif arguments_list[0] not in EduPahtwayommand.classes:
                    print("** class doesn't exist **")
                    continue  # Skip this iteration

                # Create a new instance of the specified class (Course)
                new_instance = globals()[arguments_list[0]]()

                # Set the attributes of the new instance from the arguments
                for my_args in arguments_list[1:]:
                    # Only split at the first '=' to correctly parse the key-value pair
                    key, value = my_args.split("=", 1)
                    # Remove surrounding quotes if present
                    value = value.strip("'")
                    setattr(new_instance, key, value)

                # Simulate saving the instance and assigning an ID
                new_instance.save()

                # Print the newly created course ID
                print(f"Created new course with ID: {new_instance.id}")
                
                # Wait for 3 seconds before creating the next course
                time.sleep(1)
            
            except Exception as e:
                print(f"Error creating course: {e}")
                pass


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


