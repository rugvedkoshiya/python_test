# zip function combine multiple list into list using tuple
user_id = ['user1', 'user2', 'user3']
names = ['Rugevd', 'Shyam','Grey']
passwords = ['rugved123', 'shyam123']

print(list(zip(user_id,names,passwords))) # there are only two tuple because passwords has only 3rd value.
# we can convert also in dictionary if there are only two list for zipping.

# now we unzipping... (* Oprater with zip function)
l = [(1,2),(2,3),(4,5),(6,7)]
l1, l2 = list(zip(*l))
print(l1) # Output : (1, 2, 4, 6)
print(list(l2)) # Output : [2, 3, 5, 7]

# now we find maximmum among l1 and l2 
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list) # Output : [2, 3, 5, 7]