# we can use sort function for mutable, but for non mutable we use sorted function
fruits1 = ['graps', 'mango', 'apple']
fruits1.sort()
print(fruits1) # Output : ['apple', 'graps', 'mango']

fruits2 = ('graps', 'mango', 'apple')
print(sorted(fruits2)) # Output : ['apple', 'graps', 'mango']
print(fruits2) # Output : ('graps', 'mango', 'apple')

fruits3 = {'graps', 'mango', 'apple'}
print(sorted(fruits3)) # Output : ['apple', 'graps', 'mango']
print(fruits3) # Output : ('graps', 'mango', 'apple')

mobiles = [
    {'model' : 'Realme 3 Pro', 'price' : 14000},
    {'model' : 'iPhone 11 Max Pro', 'price' : 90000},
    {'model' : 'One Plus 7 Pro', 'price' : 55000}
]
sorted_mobiles = sorted(mobiles, key = lambda item : item.get('price'))
print(sorted_mobiles) # Output : [{'model': 'Realme 3 Pro', 'price': 14000}, {'model': 'One Plus 7 Pro', 'price': 55000}, {'model': 'iPhone 11 Max Pro', 'price': 90000}]
