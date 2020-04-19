# If we want to use function with all parameters then we must follow this order :
# normal parameters
# *args parameters
# default parameters
# **kwargs parameters

def func(name, *args, last_name = 'Unknown',  **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('Rugved', 1,2,3, a=1,b=2)
# Output :
# Rugved
# (1, 2, 3)
# Unknown
# {'a': 1, 'b': 2}