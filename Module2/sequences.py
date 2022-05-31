# List
# friends = ["Samar", "Sagar", "Peehu", "Heena", "Ram"]
# print(hex(id(friends)))
# # Indexing
# # print(friends[1])
# # # Slicing
# # print(friends[2:4])
# # print(friends[-1])
# # print(len(friends))
# # List is mutable
# friends.append("Anne")
# print(friends)
# print(hex(id(friends)))
# friends.insert(2, "Raman")
# print(friends)
# more_friends = ['Shilpi', 'Rohit', 'Priya']
# friends.extend(more_friends)
# print(friends)
# friends.remove('Anne')
# print(friends)
# friends.pop(4)
# print(friends)
#
# # Searching
# print(friends.index('Shilpi'))
# print('Raman' in friends)
#
# # Operators
# numbers = [1, 4, 5, 6, 7]
# numbers2 = [4, 8, 9, 67]
# all_numbers = numbers + numbers2
# print(all_numbers)
# print(numbers*3)

# Tuple
# friends = ("Samar", "Sagar", "Peehu", "Heena", "Ram", "Sagar")
# print(type(friends))
# print(friends.count("Sagar"))
#
# students = ("Simran", "Virat", "Raj", ["Shalu", "Raj", "Peter"])
#
# print(type(students))
# print(hex(id(students)))
# print(type(students[3]))
# print(hex(id(students[3])))
# print(hex(id(students[2])))
# students[3].append("Shyam")
# print(hex(id(students[3])))
# students[3][1] = "Samar"
# print(students)


# Dictionary

# students = {
#             "Samar": [34, 45, 37, 48, 29],
#             "Priya": [32, 26, 49, 48, 39],
#             "Anne": [32, 26, 49, 48, 39]
#             }
#
# print(students["Samar"])
# students["Samar"] = [39, 45, 50, 49, 21]
# print(students)
# students["Santosh"] = [39, 45, 50, 49, 21]
# print(students)
# students.pop("Santosh")
# print(students)
# students.update({'Priya': [1,2,34,5,6]})
# print(students)
# print(students.get("Heena", [1,2,3,45,6]))

# Sets


friends = {"Samar", "Sagar", "Peehu", "Heena", "Ram", "Ram"}
close_friends = {"Sagar", "Sumona", "Shankar"}
print(friends)
# friends.pop()
# print(friends)
print(friends.union(close_friends))
print(friends.intersection(close_friends))
print(friends.difference(close_friends))
print(close_friends.difference(friends))
for friend in friends:
    print(friend)

