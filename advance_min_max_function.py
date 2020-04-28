names = ['Rugved','Shyam','Grey']
print(max(names, key = lambda item : len(item))) # Output : Rugved
print(min(names, key = lambda item : len(item))) # Output : Grey

# Let's do it in dictionaries inside list
user1 = [
    {'name' : 'Rugved', 'score' : 90, 'age' : 18},
    {'name' : 'Shyam', 'score' : 80, 'age' : 23},
    {'name' : 'Grey', 'score' : 85, 'age' : 100}
]
print(max(user1, key = lambda item : item.get('score'))['name']) # Output : Rugved
print(max(user1, key = lambda item : item.get('age'))['name']) # Output : Grey
print(min(user1, key = lambda item : item.get('score'))['name']) # Output : Shyam

# Let's do it in dictionaries inside dictionaries
user2 = {
    'Rugved' : {'score' : 90, 'age' : 18},
    'Shyam' : {'score' : 80, 'age' : 23},
    'Grey' : {'score' : 85, 'age' : 100}
}
print(max(user2, key = lambda item : user2[item]['score'])) # Output : Rugved
print(max(user2, key = lambda item : user2[item]['age'])) # Output : Grey
print(min(user2, key = lambda item : user2[item]['score'])) # Output : Shyam