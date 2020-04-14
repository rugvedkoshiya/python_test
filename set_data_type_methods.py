# Add method in set data type
s1 = {1,2,3}
s1.add(4)
s1.add(5)
s1.add(4) # It's not add because set is unique collection of item
print(s1) # Output : {1, 2, 3, 4, 5}
# -----------------------------------------------------
# Remove Method
s2 = {1,2,3}
s2.remove(3)
print(s2) # Output : {1, 2}
# s2.remove(4) # It's show Error
# -----------------------------------------------------
# Discard Method
s3 = {1,2,3}
s3.discard(3)
print(s3) # Output : {1, 2}
s3.discard(4) # It's not shown Error, that's the diffrence between remove method and discard method
# -----------------------------------------------------
# clear method
s3.clear() # It's clear the set
print(s3) # Output : set()
# -----------------------------------------------------
# copy method
s2_copy = s2.copy()
print(s2_copy) # Output : {1, 2}