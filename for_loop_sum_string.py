total = 0
user_input = input("Enter Your Number : ")
for i in range(0, len(user_input)):
    total += int(user_input[i])
print(total)