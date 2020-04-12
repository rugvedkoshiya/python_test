user_info = {
        'name' : 'Rugved',
        'age' : 18,
        'color' : ['Blue','Black']
    }

user_info_values = user_info.values()
print(user_info_values) # Output : (['name', 'age', 'color'])
print(type(user_info_values)) # Output : <class 'dict_keys'>
for i in user_info:
    print(user_info[i]) # It print values of the keys