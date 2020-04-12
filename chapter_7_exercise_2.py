from os import system, name # It's for clear function
def clear(): # It's for clear function
    if name == 'nt':  # It's for clear function
        _ = system('cls') # It's for clear function
user_info = {'Name' : input("Enter Name : "), 'Age' : input("Enter Age : "), 'Fav Song' : input("Enter fav Song Here : ").split(',')}
clear() # It's for clear function
for key, values in user_info.items():
    print(f"{key} : {values}")   