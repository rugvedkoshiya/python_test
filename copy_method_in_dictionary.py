sample = {'name' : 'Rugved', 'age' : 18}

sample_copy = sample.copy()
print(sample_copy) # Output : {'name': 'Rugved', 'age': 18} # this do copy

sam = sample # this do both Dictionaries same
print(sam) # Output : {'name': 'Rugved', 'age': 18}

print(sam is sample) # True
print(sample_copy is sample) # False

sam.popitem()
print(sample) # Output: {'name': 'Rugved'}
# if we do some opration with sam then it's also work with sample automatically