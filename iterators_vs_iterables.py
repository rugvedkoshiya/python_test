numbers = [1,2,3,4] # tupels, string,list,etc.. ------> Iterators
squares = map(lambda a : a**2, numbers) # map.filter -------> Iterables

# How for loop works :
# Step 1 : call iter function
# Step 2 : iter(numbers)
# Step 3 : next(iter(numbers))

# How for loop works with iterators
numbers_iter = iter(numbers)
print(next(numbers_iter)) # Output : 1
print(next(numbers_iter)) # Output : 2
print(next(numbers_iter)) # Output : 3
print(next(numbers_iter)) # Output : 4

# How for loop works with Iterables
print(next(squares)) # Output : 1
print(next(squares)) # Output : 4
print(next(squares)) # Output : 9
print(next(squares)) # Output : 16