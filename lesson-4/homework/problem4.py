import random

while (True):
    num = random.randint(1,101)
    attempts=0
    while (attempts<10):
        guess=int(input("Your guess:"))
        if (guess>num):
            print("Too high!")
        elif (guess<num):
            print("Too low!")
        else:
            print("You guessed it!")
            break
        attempts+=1
    if (attempts==10):
        print("You lost. Want to play again?")
    again = input("(Y/YES/y/yes/ok):").lower()
    if again not in ['y','yes','ok']:
        break
    