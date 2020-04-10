#  It's For Remove Space in Varible OR String
name = "     Rugved     "
dots = "....."
print(name + dots) # Not Remove any Spaces
print(name.lstrip() + dots) # Remove Left Side Spaces
print(name.rstrip() + dots) # Remove Right Side Spaces
print(name.strip() + dots) # Remove Both Lest & Right Side Spaces
print("   Rug   ved   ".strip() + dots) # It's Not Remove Middle Spaces

# For Remove All Spaces Use Replace method
print("   Rug   ved   ".replace(" ","") + dots)