# Without Enumerat Function
names = ['Rugved', 'Grey', 'Shyam']
def func1(names):
    pos = 0
    for name in names:
       print(f"{pos} ---> {name}")
       pos += 1
func1(names)
# Output :
# 0 ---> Rugved
# 1 ---> Grey
# 2 ---> Shyam

# With enumerat Function
for pos, name in enumerate(names):
    print(f"{pos} ---> {name}")
# Output :
# 0 ---> Rugved
# 1 ---> Grey
# 2 ---> Shyam