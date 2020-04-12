user_info = {
        'name' : 'Rugved',
        'age' : 18,
        'color' : ['Blue','Black']
    }
popped = user_info.pop('color') # It's return the value of popped keys
print(user_info) # Output : {'name': 'Rugved', 'age': 18}
print(popped) # Output : ['Blue', 'Black']

# Note if not pass any argument then it's show Error. because dictionaries is not ordered way collection. so can't decide last key