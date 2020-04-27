# zip function combine multiple list into list using tuple
user_id = ['user1', 'user2', 'user3']
names = ['Rugevd', 'Shyam','Grey']
passwords = ['rugved123', 'shyam123']

print(list(zip(user_id,names,passwords))) # there are only two tuple because passwords has only 3rd value.
# we can convert also in dictionary if there are only two list for zipping.