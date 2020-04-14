# Old Method
list_1 = ['abc','pqr','xyz']
reverse_1 = []
for i in list_1:
    reverse_1.append(i[-1::-1])
print(reverse_1) # Output : ['cba', 'rqp', 'zyx']


# New Method(list comprehension)
reverse_2 = [i[-1::-1] for i in list_1]
print(reverse_2) # Output : ['cba', 'rqp', 'zyx']