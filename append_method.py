# It's add items in our List Last
fruits = ["graps", "mango"]
fruits.append("apple")
print(fruits) # Output : ['graps', 'mango', 'apple']

# In Real Life Append Method Use
color = []
color.append("Red")
color.append("Green")
color.append("Blue")
color.append("Yellow")
color.append("Red")
print(color) # Output : ['Red', 'Green', 'Blue', 'Yellow', 'Red']

# List ma List
fruits1 = ['apple', 'mango']
fruits2 = ['orange', 'grapes']
fruits1.append(fruits2)
print(fruits1) # Output :  ['apple', 'mango', ['orange', 'grapes']]