
# file = open("module2.txt", "r")
# if file:
#     print("File opened successfully")
#     content = file.read()
#     print(content)
#     file.close()
#

data = ("Samar", "Sagar", "Peehu", "Heena", "Ram", "Sagar")
print(list(enumerate(data, start=1)))

with open("module2.txt", "r") as file:
    print("File opened successfully")
    for line, data in enumerate(file, start=1):
        print(f"Line Number: {line} Data: {data}")

# with open("module2.txt", "r") as file:
#     # content = file.readline()
#     # print(content)
#     #print(file.readlines())
#     for f in file.readlines():
#         print(f)

#     print(content)
#     content = file.read(20)
#     print(content)
#     print(file.closed)
#
# print(file.closed)

with open("file1.txt", "w") as file:
    file.write("Hello World.\nThis is Module3sasasas")
    print(file.tell())
    file.seek(10)
    file.write("\nThis data is appended")

with open("file1.txt", "a") as file:
    file.write("\nThis data is appended")
