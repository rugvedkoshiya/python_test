def multiply(*args):
    mul = 1
    for i in args:
        mul *= i
    return mul

nums = [2,3,4]
print(multiply(nums)) # Output : [2, 3, 4] # Means our function is not working
print(multiply(*nums)) # Output : 24 # Means our function is working