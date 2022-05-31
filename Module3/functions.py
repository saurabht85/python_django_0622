# Functions

# def greet(name):
#     print(f"Hello {name}")
#
# greet(input("Enter your name: "))

def is_odd(x):
    if x%2 != 0:
        return True

# num = int(input("Enter a number: "))
# if is_odd(num):
#     print(f"{num} is odd")

# Types of Arguments
#1. Positional/Required Params

# def add(x,y):
#     return x+y
#
# print(add(2,5))

# Keyword Arguments

# def student(name, age, marks):
#     average_marks = sum(marks)/len(marks)
#     return f"Student: {name}, age: {age}, Average Marks: {average_marks}"
#
# print(student(age=23, name="Saurabh", marks=[45, 23, 67, 45]))

# Default Argument
# def student(name, marks, age=20):
#     average_marks = sum(marks)/len(marks)
#     return f"Student: {name}, age: {age}, Average Marks: {average_marks}"
#
# print(student(name="Saurabh", marks=[45, 23, 67, 45], age=23))

# Arbitrary Arguments / Variable Length Arguments

# *args, **kwargs

# def mult(*args):
#     res = 1
#     print(type(args))
#     for num in args:
#         res = res * num
#     return res
#
# print(mult(2,3, 4, 5, 2))
#
#
# def students(**kwargs):
#     for key, value in kwargs.items():
#         print(f"Key is: {key}")
#         print(f"Value is {value}")
#
# students(Name="Saurabh", Age=34, avg_marks=65)

# Call by reference and Call by value

# def change_string(name):
#     print(f"Inside fun: {name}")
#     name = "New name"
#     print("Inside Function change name")
#     print(name)
#     return name
#
# name = "Saurabh"
# print("Outside Function call")
# print(name)
# change_string(name)
# print(name)

# def avg_marks(*args):
#     return sum(args)/len(args)
#
# print(avg_marks(10,12,15,9))

# def change_list(lis):
#     print(f"Inside func: {lis}")
#     lis.append("New Value")
#     print(f"Inside func2: {lis}")
#
# lis = ["Hello", "There"]
# print(f"Outside func {lis}")
# change_list(lis)
# print(f"Outside func {lis}")

# Lambda Functions
# Higher Order Functions: Accepts another function as an argument
# First Class Functions: Can be passed as an argument to Higher Order Functions

x = lambda a, b: a+b

print(x(40, 30))

# Filter
#
# list_of_nums = list(range(1, 21))
# oddlist = list(filter(lambda x:(x%2!=0), list_of_nums))
# print(oddlist)

# Map
list_of_nums = list(range(1, 21))
squared_nums = list(map(lambda x: x**2, list_of_nums))
print(squared_nums)

def odd_nums(x):
    return x%2 !=0

list_of_nums = list(range(1, 21))
oddlist = list(filter(odd_nums, list_of_nums))
print(oddlist)