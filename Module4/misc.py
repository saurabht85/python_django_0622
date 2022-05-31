# Decorators

user_role = {'sam': 'admin',
             'priya': 'hr'}

def authenticate(func):
    def inner(*args, **kwargs):
        user = input("Enter username: ")
        if user_role.get(user, None) == 'admin':
            return func(*args, **kwargs)
        else:
            return("You are not authenticated")
    return inner

@authenticate
def update_name(name, new_name):
    name = new_name
    return name

name = "Saurabh"
new_name = update_name(name, "Rakesh")
print(new_name)