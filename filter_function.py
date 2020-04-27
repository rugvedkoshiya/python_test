# Filter Function with difining function
def is_even(a):
    return a%2 == 0

numbers = [1,2,3,4,5,6,7,8,9]
even1 = list(filter(is_even, numbers))
print(even1) # Output : [2, 4, 6, 8]

# Flter function with lambda expression
even2 = list(filter(lambda a : a%2 == 0, numbers))
print(even2) # Output : [2, 4, 6, 8]

# Let's learn about Iterators...
# we can's print means access too many time, we can access only one time in filter or map function
# but if we convert it into list or tuple then we can access infinite time which is done in upper code.

even3 = filter(lambda a: a%2 == 0, numbers) #In this it will access only one time.
for i in even3:
    print(i)

for i in even3:
    print(i)