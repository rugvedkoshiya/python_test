# Old Method
list_1 = [True, [1,2], 1,'Rugved',2.0,3]
final_list = []
for i in list_1:
    if type(i) == int or type(i) == float:
        final_list.append(str(i))
print(final_list) # Output : ['1', '2.0', '3']


# New Method(list comprehension)
final_list_2 =[str(i) for i in list_1 if type(i) == int or type(i) == float]
print(final_list_2) # Output : ['1', '2.0', '3']