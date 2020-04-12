user_info = {
        'name' : 'Rugved',
        'age' : 18,
        'color' : ['Blue','Black']
    }
user_items = user_info.items()
print(user_items) # Output : ([('name', 'Rugved'), ('age', 18), ('color', ['Blue', 'Black'])])
print(type(user_items)) # Output : <class 'dict_items'>

for i, j in user_items:
    print(f"Key is {i} and Values is {j}")

# Output :
# Key is name and Values is Rugved
# Key is age and Values is 18
# Key is color and Values is ['Blue', 'Black']