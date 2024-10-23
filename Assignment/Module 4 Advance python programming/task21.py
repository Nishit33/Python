#  What are oops concepts? Is multiple inheritance supported in java 

"""
OOP Concepts:



Encapsulation:

It refers to bundling the data (attributes) and the methods (functions) that manipulate the data into a single unit, typically a class.
Access control is an important part of encapsulation, which hides the internal state of the object and protects the object's integrity by restricting access to its attributes directly.




Abstraction:

It simplifies complex systems by hiding the unnecessary details and exposing only the essential functionalities.
Abstract classes and interfaces are often used in Java and other OOP languages to achieve abstraction. 
They provide a way to define what an object can do without specifying how it will do it.




Inheritance:

This is a key feature of OOP where one class (called the child or subclass) derives properties and behavior (methods) from another class (called the parent or superclass).
Inheritance promotes code reusability by allowing common functionality to be defined in a base class and inherited by derived classes.




Polymorphism:

It refers to the ability of different objects to respond in their own way to the same method call.
Compile-time polymorphism (method overloading) occurs when multiple methods have the same name but different signatures.
Runtime polymorphism (method overriding) occurs when a subclass provides its own implementation of a method that is already defined in its superclass.





Multiple Inheritance:

Multiple inheritance allows a class to inherit properties and behavior from more than one parent class. 
This can lead to ambiguity (the Diamond Problem) when a class inherits from two classes that have methods with the same name.




Java's Approach:

Java does not support multiple inheritance using classes to avoid the Diamond Problem.
Instead, Java supports multiple inheritance through interfaces. 
A class can implement multiple interfaces, thus inheriting behaviors from multiple sources.
"""