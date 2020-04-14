# We want this...
# d = {1:'Odd', 2:'Even'}
d = {i:('Even' if i%2 == 0 else 'Odd') for i in range(1,11)}
print(d) # output : {1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd', 6: 'Even', 7: 'Odd', 8: 'Even', 9: 'Odd', 10: 'Even'}