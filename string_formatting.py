name = input("Enter Your Name : ")
age = input("Enter Your Age : ")
print("Hello " + name + " Your age is " + age) # Ugly Syntex # input is already in string # Python 2
print("Hello {} Your age is {}".format(name, age)) # Simple Syntex # Python 3
print(f"Hello {name} Your age is {age}") # very Simple Syntex # Python 3.6 and Leter # Never Forgot f
# You can also Use Calculation on it. like...
print("Hello {} Your age is {}".format(name, int(age)+6)) # Convert in Integer
print(f"Hello {name} Your age is {int(age)+6}") # Convert in Integer