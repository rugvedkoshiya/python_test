def is_even(a):
    return a%2 == 0
print(is_even(6)) # Output : True

is_even2 = lambda a : a%2 == 0
print(is_even2(6)) # Output : True

# -------------------------------------------

def  func(s):
    if len(s) > 5:
        return True
    else:
        return False
print(func('Rugved')) # Output : True

func2 = lambda s : True if len(s) > 5 else False
print(func2('Rugved')) # Output : True