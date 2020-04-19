def func(names, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in names]
    else:
        return [name.title() for name in names]

name = ['rugved','shyam']
print(func(name)) # Output : ['Rugved', 'Shyam'
print(func(name, reverse_str=True)) # Output : ['Devgur', 'Mayhs']