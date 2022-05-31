
#IF Else

# age = int(input("Enter your age: "))

# if age > 18:
#     print("You are eligible to vote")
# else:
#     print("Not eligible")

# if age > 18:
#     print("You are eligible to vote")
# elif age == 18:
#     print("Need to wait few more months")
# else:
#     print("Not Eligible")

# Loops

# While
# i = 1
# while i <= 10:
#     print(f"{i} to the power2 is : {i**2}")
#     i += 1

# while True:
#     age = int(input("Enter your age: "))
#     if age > 10:
#         print("Valid age")
#         break
#     else:
#         print("Invalid age, try again.")

# For
# you need a sequence/set

friends = ["Samar", "Sagar", "Peehu", "Heena", "Ram"]
for friend in friends:
    print(friend)

for i in range(5):
    print(i**3)

for i in range(1, 20):
    if i == 10:
        continue
    if i % 2 == 0:
        print(f"{i} is a even number")
