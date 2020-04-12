# It's our Dictionariy
user_info = {
    'name' : 'Rugved',
    'age' : 18,
    'color' : ['Blue','Black']
}
# Checking for Keys... (It's not check values)
if 'name' in user_info: # This Gives Present
    print("Present")
else:
    print("Not Present")
# ----------------------------------------
# Checking for values... (It's not check keys)
if 'Rugved' in user_info.values(): # This Gives Present
    print("Present")
else:
    print("Not Present")
# ----------------------------------------
if 18 in user_info.values(): # This Gives Present
    print("Present")
else:
    print("Not Present")
# ----------------------------------------
if ['Blue','Black'] in user_info.values(): # This Gives Present (we can check lists also)
    print("Present")
else:
    print("Not Present")