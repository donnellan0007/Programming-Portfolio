import random

#This is the function that has the logic for the random number. 
def roll_dice(num):
    return random.randint(1, num)

#This is the while loop to ensure that the program will continue running forever
#Try/Excepts are used for ValueErrors, and it will just go back to the program
while True:
    try:
        print(roll_dice(int(input("Number here: "))))
    except ValueError:
        print("Invalid response. Please choose a number, not a string")
        print(roll_dice(int(input("Number here: "))))
