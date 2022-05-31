
"""
class ClassName:
    <<initializer>>
    <<statement1>>

    <functions>

"""

# Inheritance

# class Student:
#     """
#     Class to store students
#     """
#
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#     def __str__(self):
#         return f"Student name: {self.name} - age: {self.age} - course: {self.course}"
#
#     def print_details(self):
#         print(50*"*")
#         print(f"Student name: {self.name}")
#         print(f"Student age: {self.age}")
#         print(f"Student Course: {self.course}")
#         print(50*"*")
#
#     def average_marks(self, marks):
#         return f"{self.name} average marks: {sum(marks)/len(marks)}"
#
#
# class WorkingStudent(Student):
#     def __init__(self, name, age, course, stipend):
#         super().__init__(name, age, course)
#         self.stipend = stipend
#
#     def print_stipend(self):
#         return f"{self.name} stipend is {self.stipend}"
#
#
# student1 = Student(name="Saurabh", age=34, course="CS")
# print(student1)
# student1.print_details()
# print(student1.name)
#
# print(student1.average_marks([76, 89, 45, 87, 65]))
# student2 = Student(name="Vibhor", age=24, course="ME")
# student2.print_details()
# print(student2.name)
#
# working1 = WorkingStudent("Sam", 31, "CS", 8000)
# working1.print_details()
# print(working1.print_stipend())

# Multiple Inheritance

# class Calc:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def summation(self):
#         return self.a + self.b
#
# class Calc1:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def multiply(self):
#         return self.a * self.b
#
#
# class Calculator(Calc, Calc1):
#
#     def __init__(self, a, b):
#         super(Calc, self).__init__(a, b)
#         #super(Calc1, self).__init__(a, b)
#     def divide(self):
#         return self.a/self.b
#
# c = Calculator(30, 20)
# print(c.summation())
# print(c.multiply())
# print(c.divide())
#
#
# # Multi level inheritance
#
# class Animal:
#     def speak(self):
#         print("Animal speaking")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# class Pup(Dog):
#     def eat(self):
#         print("Pup eats")
#
# p1 = Pup()
# p1.eat()
# p1.bark()
# p1.speak()

# Polymorphism

# print(len("Saurabh"))
# print(len([1,2,3,4,5,6 ]))
# print(len({"name": "Saurabh", "age": 34}))

# Method overriding
# class Bank:
#     def getroi(self):
#         return 10
#
# class SBI(Bank):
#     def getroi(self):
#         return 8
#
# class ICICI(Bank):
#     def getroi(self):
#         return 7

# class Bank:
#     def getroi(self):
#         return 10
#
# class SBI:
#     def getroi(self):
#         return 8
#
# class ICICI:
#     def getroi(self):
#         return 7
# b1 = Bank()
# s1 = SBI()
# i1 = ICICI()
#
# print(b1.getroi())
# print(s1.getroi())
# print(i1.getroi())

# Data Abstraction
#
# class Employee:
#     __count = 0
#     name = "Gaurav"
#     def __init__(self):
#         Employee.__count = Employee.__count + 1
#         print(Employee.name)
#     def display(self):
#         print(f"Number of employees: {Employee.__count}")
#
# emp1 = Employee()
# emp2 = Employee()
# emp1.display()
# print((emp1._Employee__count))
# print(emp1.name)
# print(Employee.name)
#
# # Methods in Python
# # Static method
#
# class Student:
#     """
#     Class to store students
#     """
#
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#     def __str__(self):
#         return f"Student name: {self.name} - age: {self.age} - course: {self.course}"
#
#     def print_details(self):
#         print(50*"*")
#         print(f"Student name: {self.name}")
#         print(f"Student age: {self.age}")
#         print(f"Student Course: {self.course}")
#         print(50*"*")
#
#     @staticmethod
#     def average_marks(marks):
#         return f"average marks: {sum(marks)/len(marks)}"
#
# print(Student.average_marks([56, 76, 98, 67, 87]))
#
# # Class method
#
# class TestClass:
#     def __init__(self):
#         print("Hello World")
#
#     @classmethod
#     def example(cls):
#         print("Inside class method")
#         cls.print_details()
#
#     @staticmethod
#     def print_details():
#         print("Hello i am in print details function")
#
# #TestClass.example()
#
#
# class Derived(TestClass):
#
#     @staticmethod
#     def print_details():
#         print("Hello i am in print details function of Derived")
#
# Derived.example()

class Garage:

    def __init__(self, cars):
        self.cars = list()
        self.cars.append(cars)

    def __str__(self):
        return f"Garage with {len(self.cars)} cars"

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]


honda_garage = Garage("City")

honda_garage.cars.append("Civic")
print(honda_garage[1])
print(len(honda_garage))
print(honda_garage)