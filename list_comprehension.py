# Old Method
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares) # Output : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# New Method (list comprehension)
squares2 = [i**2 for i in range(1,11)]
print(squares2) # Output : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Old Method
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative) # Output : [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
# New Method (list comprehension)
negative2 = [-i for i in range(1,11)]
print(negative2) # Output : [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]


# Old Method
names = ['Rugved','Shyam','Grey']
new_names = []
for i in names:
    new_names.append(i[0])
print(new_names) # Output : ['R', 'S', 'G']
# New Method (list comprehension)
names2 = [i[0] for i in names]
print(names2) # Output : ['R', 'S', 'G']