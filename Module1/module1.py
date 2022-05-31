# This is a comment
# This is another comment

'''
This is a
multiline comment
'''

"""
This is another
comment
"""

# print("Hello world")
#
# print("hi there")
#
# # Integer
#
# age: int = 24
#
# print(type(age))
#
# print(10*5) # Multiplication
# print(10/5) # Division
# print(10+5) # Addition
# print(10-5) # Subtraction
# print(10 % 6) # Modulus
# print(10 ** 2)  # To the power of
# print(10//5) # Division
#
# import math
# print(math.factorial(5))
#
# # Comparison operators
# print(10 < 4) # Less Than
# print(10 > 4) # Greater Than
# print(10 == 4) # Equality
# print(10 <= 4) # Less Than Equal to
# print(10 >= 4) # Greater Than equal to
# print(10 != 5) # Not equal to
#
# # PEMDAS -> Parentheses, Exponent, Multi, Division, Add, Sub
#
# res = 20 * (10 - 9 + 8 * (6 / 2))
# print(res)

# Strings

name = "saurabh tewary test case 1"
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.split(' '))
print(name.isalpha())
print(name.title())
print(name.find("te"))
print("163w6576".zfill(16))

# String Substitution
name = "Geeta"
age = 25
print(f"Hello {name}, How are you. You are {age} years old. ")
print("Hello {name}, How are you. You are {age} years old. ".format(age=age, name=name))

print("Hello " + name + ", How are you. You are " + str(age) + " years old")

# Indexing and Slicing

name = "Saurabh Tewary"
print(name[5])
print(name[5:7])
print(name[5:])
print(name[:7])
print(name[-1])
print(name[-3:])

# Concatenation

print("Saurabh" + " Tewary")
# Repeat
print("Hello" * 3)

# Strings and Integers are immutable

a = 16
print(hex(id(a)))
a = 18
print(hex(id(a)))

b = 16

print(hex(id(b)))

b = "h"
b = "y"








