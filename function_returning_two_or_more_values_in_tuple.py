def calc(a,b): # It's Function
    add = a+b
    multiply = a*b
    return add, multiply

print(calc(2,3)) # Output : (5, 6) and It's tuple

add, multiply = calc(2,3)
print(add) # Output : 5
print(multiply) # Output  : 6