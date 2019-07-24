import random 
import math
while True:
    userInput = input("Name the person you want to play with: ")
    randomBool = ["You killed " + userInput, userInput + " survived"]
    print(random.choice(randomBool))
