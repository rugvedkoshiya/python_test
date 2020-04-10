# Step Argument
# Syntex : [Start argument:stop argument:step]

# Position (Index Number)
# R  =  0 , -6
# u  =  1 , -5
# g  =  2 , -4
# v  =  3 , -3
# e  =  4 , -2
# d  =  5 , -1

print("Rugved"[::1]) # output : Rugved
print("Rugved"[0:6:1]) # output : Rugved
print("Rugved"[0:6:]) # output : Rugved
print("Rugved"[0:6:2]) # output : Rge
print("Rugved"[0:6:3]) # output : Rv
print("Rugved"[::-1]) # output : devguR
print("Rugved"[6:2:-1]) # output : dev
print("Rugved"[6:0:-2]) # output : dvu