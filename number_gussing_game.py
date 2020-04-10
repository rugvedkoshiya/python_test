import random
winning_number = random.randint(1, 100)
user_input = int(input("Guess a Number Between 1 to 100 : "))
gusses = 1
while True:
    if user_input == winning_number:
        print(f"WOW !! You Guss Right Number in {gusses} Times")
        break
    else:
        if winning_number > user_input:
            print("You Guss Wrong Number & it's Lower than Winning Number")
        else:
            print("You Guss Wrong Number & it's Bigger than Winning Number")
        gusses += 1
        user_input = int(input("Guss Again : "))