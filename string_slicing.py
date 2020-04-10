# string Slicing / Selecting sub Sequence
# variable_name = "Rugved"
# Syntex : [start argument : stop argument]

# Position (Index Number)
# R  =  0 , -6
# u  =  1 , -5
# g  =  2 , -4
# v  =  3 , -3
# e  =  4 , -2
# d  =  5 , -1

name = "Rugved"
print(name[0:5]) # Output : Rugve
print(name[0:6]) # Output : Rugved
print(name[:]) # Output : Rugved
print(name[1:6]) # Output : ugved
print(name[3:6]) # Output : ved
print(name[-6:-1]) # Output : Rugve
print(name[-3:-1]) # Output : ve
print(name[3:]) # Output : ved
print(name[0:3]) # Output : Rug