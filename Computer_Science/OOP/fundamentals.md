# OOP Fundamentals

## Introduction

OOP is a programming paradigm that organizes software around objects rather than functions and logic. An object contains both data (attributes) and methods (behavior) making programs more modular, reusable and easier to understand and manage.

## Classes

A class is a blueprint or template used to create objects. It defines the properties/attributes/data objects are represented as and the methods they can perform.

A class does not occupy memory until an object is created.

A Car represents a class while a BMW could be an object created from that class.

## Objects

An object is an instance of a class. It represents a real-world entity and can access the properties and methods defined in a class.

Occupies memory when created.

## Encapsulation

Encapsulation is the process of binding data and methods together into a single unit and restricting direct access to data using access modifiers.

Improves security, and access data through getter and setter methods.

Ex:

```python
class Employee:
    def __init__(self):
        self.__salary = 0 # Private data

    def setSalary(self, salary): # setter for data
        self.__salary = salary

    def getSalary(self): # getter for data
        return self.__salary
```

## Abstraction

Abstraction hides implementation details and shows only the essential features of an object.

Improves code simplicity, and achieved using abstract classes and interfaces.

- **Abstract Class:**
  - A class that cannot be instantiated directly to create an object
  - It serves as an incomplete blueprint or base class designed to be inherited by other concrete subclasses
  - Ex: Animal
- **Interface:**
  - Can't be instantiated into an object as well
  - A code contract that the classes whom use it must implement methods of

Ex: An ATM machine is like an example of a real world abstraction where a user interacts with simple operations on the screen while internal working and implementation details remain hidden.

## Inheritance

Allows one class to acquire the properties and methods of another class.

This establishes a **parent-child relationship** and supports **method overriding**

Ex: Dog, Cat, Cow, can all be derived from the parent Animal class.

Ex:

```python
class Animal: # parent class
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal): # child class
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.sound()
dog.bark() # the child inheritted the parents sound method
```

## Polymorphism

The term itself means "many forms" and in OOP is allows the same method or interface to perform different actions depending on how the object invokes it. This feature improves flexability in applications.

Achieved with:

- **method overloading:**
  - Lets a class have multiple methods with the same name as long as their parameter lists are different
  - This is a form of compile-time(static) polymorphism
- **method overridng:**.
  - Lets a child class have a specific implementation of a method that is already defined in its _super class_ aka it's parent

Ex:

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```
