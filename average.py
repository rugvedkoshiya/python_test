# Long Process
num1 = input("Enter the First Number : ")
num2 = input("Enter the Second Number : ")
num3 = input("Enter the Third Number : ")
print(f"The Average of Your Three Number is : {(int(num1) + int(num2) + int(num3)) / 3}") # Never forgot f
# Short Process
num1, num2, num3 = input("Enter Your Three Number Using Space : ").split()
print(f"The Average of Your Three Number is : {(int(num1) + int(num2) + int(num3)) / 3}") # Never forgot f