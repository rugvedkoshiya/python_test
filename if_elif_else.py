# Show Ticket Pricing

age = input("Enter Your age : ")
age = int(age)
if age==0:
    print("You can't Watch")
elif 0<age<=3:
    print("Ticket Price : Free")
elif 3<age<=10:
    print("Ticket Price : 100 Rs")
elif 10<age<=18:
    print("Ticket Price : 150 Rs")
elif 18<age<=50:
    print("Ticket Price : 200 Rs")
else:
    print("Ticket price : 150 Rs")