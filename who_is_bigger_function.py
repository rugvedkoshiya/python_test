def big(a,b,c):
    if b < a and c < a:
        return a
    elif a < b and c < b:
        return b
    else:
        return c

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number :"))
num3 = int(input("Enter Third Number : "))
print(f"{big(num1,num2,num3)} is Big")
