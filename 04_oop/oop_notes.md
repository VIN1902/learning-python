# Class
- A structure/blueprint for a real world entity.
- You define the entity's properties/attribute (variables) and behaviour (methods/funcitons).
- Example: A blank bank form.

# Object
- An instance of the blueprint.
- Instance = a single occurence of our structure. an example of blueprint.
- Example: A user fills that blank form and now it belongs to or is associated with them.

# Inheritance
- Borrowing/inheriting the attributes and behaviour of your parent.

# Encapsulation
- Think of a capsule, all looks the same from outside but may contain different medicine inside.
- Similarly its a technique that hides the info from outsiders and only accessible indirectly when allowed using methods (getter/setter).
- Everyone can see and interact with the capsule but can't do the same with its content without permission in form of methods.

# Polymorphism
- Methods can have same name but different behaviour/functionality.
- This is usually achieved by method overriding in a inheritance scenario.

# class variable vs static methods
- Defination:
    1. static method: A method that belongs to a class but doesn't modify instance or class variables.
    2. class variable: A variable shared by all instances of a class.
- Class variables → Store shared data.
- Static methods → Utility functions that don’t modify instance/class variables.
- Static methods CAN access class variables, but they can't modify them directly.