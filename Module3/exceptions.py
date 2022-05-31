# import sys
#
# try:
#     num1 = int(input("Enter a Number: "))
#     num2 = int(input("Enter another number: "))
#
#     print(f"Division of {num1} and {num2} is: {num1/num2}")
# except (ZeroDivisionError, ValueError):
#     #print("Cannot divide a number with 0. Please try again.")
#     print("Invalid input. Please enter a number greater than 0")
#     sys.exit(1)
# except Exception as err:
#     print(f"Unknown error: {err}")
# else:
#     print("Program ended successfully")
# finally:
#     print("Program ended")
# # except ValueError:
# #     print("Incorrect number entered. Please enter a valid numeric value")
# #     sys.exit(1)
# #
# try:
#     with open("test.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File does not exist. Please create the file first before running the program")
# #print(name)
# #import blablabla
#

# Assert Statements
def avg(marks):

    assert len(marks)!=0, "Marks should have atleast one value"
    return sum(marks)/len(marks)
print(avg([]))
print(avg([10, 20, 54, 65]))



