# Center Method
name = "Rugved"
print(name.center(8, "*")) # Output : *Rugved*
print(name.center(7, "*")) # Output : *Rugved
print(name.center(10, "*")) # Output : **Rugved**

# Let's Make One Small Programme
name = input("Enter Your Name : ")
print(name.center(len(name) + 8, "*"))