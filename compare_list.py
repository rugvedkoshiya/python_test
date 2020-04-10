# Here We have to two type for Compare List
fruits1 = ['apple','banana','pear']
fruits2 = ['orange','mango','apple','cheri','kiwi']
fruits3 = ['apple','banana','pear']
# 1. == # Ye Value Check Karta he ki value Sem he ki Nahi
print(fruits1 == fruits2) # Output : False
print(fruits1 == fruits3)# Output : True

# 2. is # ye dono list hamari memory me ek jagah par he ya nahi ye check karta hai
print(fruits1 is fruits2) # Output : False
print(fruits1 is fruits3)# Output : False