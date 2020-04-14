# We want this square = {1:1, 2:4, 3:9}
square = {num : num**2 for num in range(1,11)}
print(square) # Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
for i,j in square.items():
    print(f"Square of {i} : {j}")
# Output :
# Square of 1 : 1
# Square of 2 : 4
# Square of 3 : 9
# Square of 4 : 16
# Square of 5 : 25
# Square of 6 : 36
# Square of 7 : 49
# Square of 8 : 64
# Square of 9 : 81
# Square of 10 : 100


string = "Rugved"
word_count = {char:string.count(char) for char in string}
print(word_count) # Output : {'R': 1, 'u': 1, 'g': 1, 'v': 1, 'e': 1, 'd': 1}