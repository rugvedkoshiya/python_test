# if any of them are ture then any function return True
# if all are True then and then only all function return True
num1 = [2,4,6,8]
num2 = [1,3,5,7]
num3 = [1,2,3,4]

print(all([num%2 == 0 for num in num1])) # Output : True 
print(all([num%2 == 0 for num in num2])) # Output : False
print(all([num%2 == 0 for num in num3])) # Output : False

print(any([num%2 == 0 for num in num1])) # Output : True 
print(any([num%2 == 0 for num in num2])) # Output : False
print(any([num%2 == 0 for num in num3])) # Output : True