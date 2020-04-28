# what are doc string
# what is help function
def sums(a,b):
    '''This function takes two numbers as a input'''
    return a+b
print(sums.__doc__) # Output : This function takes two numbers as a input
print(len.__doc__) # Output : Return the number of items in a container.

# print(help(sum)) ---> it's shows help of sums but now it shows error because of some reason. that's why i am comment out it.