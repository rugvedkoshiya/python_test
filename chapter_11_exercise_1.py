def any_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't Pass Anything"
print(any_power(3,*[1,2,3])) # Output : [1, 8, 27]