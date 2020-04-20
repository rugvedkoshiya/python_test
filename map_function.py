numbers = [1,2,3,4]
squares = list(map(lambda a : a**2, numbers))
print(squares) # Output : [1, 4, 9, 16]

# Using List Comprehension
new_squares = [i**2 for i in numbers]
print(new_squares) # Output : [1, 4, 9, 16]