#  You can Store Anything in List like Float, Integer, String and More...
# Integer
numbers = [1, 2, 3, 4, 5]
print(numbers) # Output : [1, 2, 3, 4, 5]
print(numbers[0]) # Output : 1
print(numbers[1]) # Output : 2
print(numbers[4]) # Output : 5
print(numbers[0:3]) # Output : [1, 2, 3]
# Strings
words = ['one', "two", "three", 'four', 'five']
print(words) # Output : ['one', "two", "three", 'four', 'five']
print(words[0]) # Output : one
print(words[1]) # Output : two
print(words[4]) # Output : five
print(words[0:3]) # Output : ['one', 'two', 'three']
# Mixed
mix = [1, 2, 'three',"four",5]
print(mix) # Output : [1, 2, 'three',"four",5]
print(mix[0]) # Output : 1
print(mix[1]) # Output : 2
print(mix[3]) # Output : four
print(mix[0:4]) # Output : [1, 2, 'three', 'four']
#  Let's do Some Fun
mix[0:4] = "four"
print(mix) # Output : ['f', 'o', 'u', 'r', 5]
mix[0:3] = ["one", 'two', 3]
print(mix) # Output : ['one', 'two', 3, 'r', 5]