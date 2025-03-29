"""
strings are the combination of numbers, symbols, and letters, enclosed inside quotations.
Creation of String: Strings can be created by enclosing numbers, letters or special symbols inside double quotation.
It means assigning a string value to a variables.
a=('hello world')
print(a)
string methods"""
from itertools import count
from operator import index

a="hello world"
print(a)
print(type(a))

#length
print(len(a))

#count
print(a.count("e"))

#upper
print(a.upper())

#lower
print(a.lower())

#index
print(a.index("o"))

#capitalize
print(a.capitalize())

# casefold
# find
print(a.find("l"))

# format
b="my name is {}"
print(b.format("megha"))

