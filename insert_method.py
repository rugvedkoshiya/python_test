#  It's Use for Add Items in Our List in Any Place
color = ["red", 'green', 'blue']

color.insert(0, 'yellow')
print(color) # Output : ['yellow', 'red', 'green', 'blue']

color.insert(1, 'yellow')
print(color) # Output : ['red', 'yellow', 'green', 'blue'] # If First in not Running

color.insert(2, 'yellow')
print(color) # Output : ['red', 'green', 'yellow', 'blue'] # If First and Second are not Running

# How to Join two Strings

fruits1 = ['mango', 'apple']
fruits2 = ['orange', 'grapes']
fruits = fruits1 + fruits2
print(fruits)
