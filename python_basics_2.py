# -*- coding: utf-8 -*-
"""Python_Basics_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GVkOUFuV5Nr1TgoeOXshIXmLZXbI4YMa

String and List operations
"""

st = 'hello'  # st = "hello" # String declaration

st[0] # Slicing

st[-1]

st[0:3]

st[:]

pal = 'Shalmali'

pal[::-1] # Reverse string

pal[::-8]

pal = 'AIML Concepts'

pal[0:90]

l1 = [12,34,23.5,67.5,True,'hello',34] # List declarartion

print(l1)

l1.append('shalmali') # Append method

l1

l1.insert(4,'nasreen')

l1

help(l1) # Help method

l1.count(34)

l1.clear()

print(l1)

l1.index(34)

l2 = [10,20,30,40]

l1.extend(l2) # Apends List 2

l1

a = l1.pop() # Returns the last indexed value from the list
a

c = l1.remove(12) # Removes the given value from the list

c # Remove will not return value

l1

l1.pop(0)

l1

l1[:4]

t1 = (23,34,True,'hello')

print(t1)

help(t1)

t1.count(34)

t1.index('hello')

