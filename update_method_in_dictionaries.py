user_info = {
        'name' : 'Rugved',
        'age' : 18,
        'color' : ['Blue','Black']
    }
more_info ={
    'name' : 'Rugved Koshiya',
    'state' : 'Gujarat'
}
user_info.update(more_info)
print(user_info) # Output : {'name': 'Rugved Koshiya', 'age': 18, 'color': ['Blue', 'Black'], 'state': 'Gujarat'}