# get method is used for get values of keys.
# But the difference is if passing key is not available in the dictionaries then its not shown error but return Noun
sample1 = {'name' : 'Rugved', 'age' : 18}
print(sample1.get('name')) # Output : Rugved
print(sample1.get('names')) # Output : Noun
print(sample1.get('names','Not Found !')) # Output : Not Found !
# we can used get method like this...
if sample1.get('name'): # it print Present
    print("Present")
else:
    print("Not Present")
# --------------------------------------------
if sample1.get('names'): # it print not present
    print("Present")
else:
    print("Not Present")

# It's done because of the get method return True or False so thats why is statement is working