# It's can Delete item in Your List
# It's just cut item in Your List and Rreturned it
fruits = ['apple', 'orange','mango', 'kiwi', 'banana']
fruits.pop()
print(fruits) # Output : ['apple', 'orange', 'mango', 'kiwi']
popped = fruits.pop(1) # It's returned value which it's popped and we stored it in any variable
print(fruits) # Output : ['apple', 'mango', 'kiwi', 'banana']
print(popped) # We print our popped element