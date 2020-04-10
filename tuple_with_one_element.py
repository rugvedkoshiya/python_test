# Tuples are immutable
tuples1 = (1,2,3,4,5) # It's tuple
tuples2 = ('word1', 'word2','word3') # It's also tuple
mixed = (1,2,'word1',2.0) # It's also tuple

print(type(tuples1)) # Output : <class 'tuple'>
print(type(tuples2)) # Output : <class 'tuple'>
print(type(mixed)) # Output : <class 'tuple'>

tuples3 = (1) # It's not tuple its just a int
print(type(tuples3)) # Output : <class 'int'>

tuples4 = ('word') # It's not tuple its just a str
print(type(tuples4)) # Output : <class 'str'>

tuples5 =(1,) # It's tuple
print(type(tuples5)) # Output : <class 'tuple'>

tuples6 =('word',) # It's tuple
print(type(tuples6)) # Output : <class 'tuple'>