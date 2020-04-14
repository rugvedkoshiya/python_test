square = {i**2 for i in range(1,11)}
print(square) # Output : {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}


names = ['Rugved', 'Shyam', 'Grey']
first = {name[0] for name in names}
print(first) # Output : {'R', 'S', 'G'} # It's print in any ordered