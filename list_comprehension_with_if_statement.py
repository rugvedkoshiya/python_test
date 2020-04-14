# Old Method
even_nums = []
odd_nums = []
for i in range(1,11):
    if i%2 == 0:
        even_nums.append(i)
    else:
        odd_nums.append(i)
print(even_nums) # Output : [2, 4, 6, 8, 10]
print(odd_nums) # Output : [1, 3, 5, 7, 9]


# New Method(list comprehension)
even = [i for i in range(1,11) if i%2 == 0]
odd = [i for i in range(1,11) if i%2 != 0]
print(even) # Output : [2, 4, 6, 8, 10]
print(odd) # Output : [1, 3, 5, 7, 9]