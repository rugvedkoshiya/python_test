def my_sum(*args):
    if all([type(i) == int or type(i) == float for i in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Wrong Input"

print(my_sum(1,2,3,4.6)) # Output : 10.6
print(my_sum(1,2,3,'Rugved')) # Output : Wrong Input