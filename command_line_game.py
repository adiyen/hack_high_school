import random
from random import randint

numb = randint(1, 100)
user_numb = int(input("Pick a number between 1 and 100: "))
tries = 0

print(user_numb, numb)
for i in range(101):
    user_numb = int(input("Pick another number between 1 and 100: "))
    tries+=1
    if user_numb < 0 or user_numb > 100:
        print("Your number was not in range.")
    elif user_numb == numb:
        print("Good Job! You got the answer! It took you", tries, "tries!")
        break
    elif abs(user_numb - numb) <= 5:
        print("You're boiling!")
    elif abs(user_numb - numb) <= 10:
        print("You're steaming!")
    elif abs(user_numb - numb) <= 20:
        print("You're hot!")
    elif abs(user_numb - numb) <= 40:
        print("You're warm!")
    elif abs(user_numb - numb) > 40:
        print("You're not even close.")
