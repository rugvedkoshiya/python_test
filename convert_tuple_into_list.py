# We can convert tuples into list or string
# We can convert list into string or tuple
nums = tuple(range(1,11)) # It's tuple
nums_list = list(nums) # It's list
nums_string = str(nums) # It's string

print(nums_list) # Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(nums)) # Output : <class 'tuple'>
print(type(nums_list)) # Output : <class 'list'>
print(type(nums_string)) # Output : <class 'str'>