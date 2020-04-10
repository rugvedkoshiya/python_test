# We can add list inside the tuples
# We can use all methos for list like append, pop...
laptops = ('asus','dell',['hp','compac','pavilion'])

laptops[2].append('omen')
print(laptops) # Output : ('asus', 'dell', ['hp', 'compac', 'pavilion', 'omen'])

laptops[2].remove('compac')
print(laptops) # Output : ('asus', 'dell', ['hp', 'pavilion', 'omen'])