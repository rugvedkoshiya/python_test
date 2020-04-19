def multiply_nums(num1,*args):
    mul = 1
    for i in args:
        mul *= i
    return mul
print(multiply_nums(2,2,3)) # Output : 6 # Fisrt 2 is not consider in args it's consider in num1