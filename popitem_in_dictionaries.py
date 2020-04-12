user_info = {
        'name' : 'Rugved',
        'age' : 18,
        'color' : ['Blue','Black']
    }
popped = user_info.popitem() # Its' delete Rendom item in the dictionary
print(user_info) # Output : {'name': 'Rugved', 'age': 18}
print(popped) # Output : ('color', ['Blue', 'Black'])
print(type(popped)) # Output : <class 'tuple'>