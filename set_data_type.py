# set is unordered collection of unique data types
# we can't store list or dictionaries in set
s1 = {1,2,3,4}
print(s1) # Output : {1, 2, 3, 4}
s2 = {1,2,3,3,4}
print(s2) # Output : {1, 2, 3, 4}
# ----------------------------------------
# How to convert list to unique
list1 = [1,2,3,3,3,4,5,5,6,7]
s3 = set(list1)
print(s3) # Output : {1, 2, 3, 4, 5, 6, 7}
s4 = list(set(list1))
print(s4) # Output : [1, 2, 3, 4, 5, 6, 7]