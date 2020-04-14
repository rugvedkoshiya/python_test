# Old Method
list_1 = []
for i in range(1,11):
    if i%2 == 0:
        list_1.append(i**2)
    else:
        list_1.append(-i)
print(list_1) # Output : [-1, 4, -3, 16, -5, 36, -7, 64, -9, 100]


# New Method(list comprehension)
list_2 = [i**2 if i%2 == 0 else -i for i in range(1,11)]
print(list_2) # Output : [-1, 4, -3, 16, -5, 36, -7, 64, -9, 100]