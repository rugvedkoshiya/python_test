# a = int(input("Enter first 7 Number : "))
# for i in range(10):
#     print(a+i)
# # for i in range(1, 11):
# #     print(f"Rugved Koshiya {i}")
from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

for tciNymbers in range(0,50000):
	print('+91', random_with_N_digits(10))