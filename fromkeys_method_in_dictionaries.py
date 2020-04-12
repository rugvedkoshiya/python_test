# It's use for create dictionaries 
# where all values are same for every key means it's used for create default dictionaries.
# where value can be anything string or int or lists or tuple.....

sample1 = dict.fromkeys(['name','age','height'],'unknown')
print(sample1) # Output : {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

sample2 = dict.fromkeys("abc",'null')
print(sample2) # Output : {'a': 'null', 'b': 'null', 'c': 'null'}

sample3 = dict.fromkeys(('name','age','weight'),'null')
print(sample3) # Output : {'name': 'null', 'age': 'null', 'weight': 'null'}