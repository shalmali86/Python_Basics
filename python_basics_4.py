# -*- coding: utf-8 -*-
"""Python_Basics_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fKl6C2C1FZuW1-MqMcrR4CNTYhDKY7zm

**Object Oriented Programming Concepts in Python**

---
"""

class Employee:  #class name
  def __init__(self,id):
    '''this is an Example Function in python'''
    self.id=id

  def add_two(self,a,b):
   return a+b

Employee  #class name

employee1 = Employee(1002)  #object creation
employee1

employee1.id  #accessing the attribute

employee1.add_two(3,4)  #calling the method

e2 = Employee(2)  #object creation
e2

e2.add_two(6,7)  #calling the method

class Person:  #class name
  def __init__(self):
    print('inside __init__()')
  def add(self,id):
    return id ** 2

p1 = Person()  #object creation
p1.add(3)

class Employee:  #class name
  def __init__(self,id):
    print('inside __init__()')
    print(f'self = {self}')
    self.id = id

E1 = Employee(1002)  #object creation
print(f'E1 = {E1}')

E1.id  #accessing the attribute

class Employee:  #class name
  def __init__(self,id,first_name,last_name):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
  def get_id(self):
    return self.id
  def get_full_name(self):
    return f'{self.first_name} {self.last_name}'

E1 = Employee(1002,'John','Doe')  #object creation
E1

E1.id  #accessing the attribute

E1.first_name  #accessing the attribute

E1.last_name  #accessing the attribute

E1.get_id()  #calling the method

E1.get_full_name()  #calling the method

#inheritance
class Developer(Employee):   #subclass
  def __init__(self,id,first_name,last_name,salary):
    super().__init__(id,first_name,last_name)
    self.salary = salary

help(Developer)

d1 = Developer(1003,'peter','deo',100000)  #object creation
d1

d1.get_full_name()  #calling the method

d1.salary  #accessing the attribute

class Myclass:
  ''' this i class level doc string '''
  def __init__(self,a,b):
    ''' this is a init dunder function'''
    self.a = a
    self.b = b
  def __habeeb__(self):
    '''This is user defined dunder function'''
    return f'{self.a} {self.b}'

m1 = Myclass('peter',20)  #object creation
m1

print(m1)  #print function

class Myclass:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __add__(self,other):
    '''hello'''
    result = self.age + other.age
    return Myclass(f'{self.name} and {other.name}',result)

m1 = Myclass('object1',56)  #object creation
m1

m2 = Myclass('object2',25)  #object creation
m2

combined = m1 + m2  #operator overloading
combined

print(combined.name)
print(combined.age )

Myclass.__add__.__doc__  #class level doc string

from teestclass import Employee  #importing the class

e1 = Employee('peter',25,4545454)

e1.name  #accessing the attribute

e1.add_two(3,4)

from teestclass import Employee