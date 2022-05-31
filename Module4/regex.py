import re

# match

# string = "Python is awesome. I love Python"
#
# matches = re.search(r'awesoe*', string)
# if matches:
#     print(matches.group())
#
# matches = re.match('Py.*is', string)
# print(matches.start())
# print(matches.end())
#
# matches = re.findall('Pyth.n', string)
# print(matches)
#
# # re.sub
# text = "Python is a very cool language"
# pattern = re.sub("cool", "good", text)
# print(pattern)
#
# text = 'hello there python alice19@gmail.com blah monkey peppa78@yahoo.com simple dane@hotmail.com'
#
# print(re.sub(r'([\w.-]+)@([\w.-]+)', r'\1@google.com', text))

# re.compile

name_check = re.compile(r"[^A-Za-z\s.]")
print(type(name_check))
name = input("Please enter your name: ")
while name_check.search(name):
    print("Invalid name. Please enter a valid name")
    name = input("Enter your name again: ")

print(f"Hello: {name}")
