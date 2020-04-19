# * is the args operator
def sums(a,b):
    return a+b
print(sums(3,4)) # Output : 7
# We cant Pass more then two arguments in the sums function
def total(*args): # We can use anything in place of args but it's covection and most of all people use args.
    tot = 0
    for num in args:
        tot += num
    print(type(args)) # Output : <class 'tuple'> # It's only foe show that the taken input is in tuple
    return tot
print(total(1,2,3,4)) # Output : 10