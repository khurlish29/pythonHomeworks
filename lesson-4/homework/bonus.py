import random

choices = ["rock", "paper", "scissors"]
userScore = 0
compScore = 0
maxScore = 5

print("Let the game start!")

while userScore < maxScore and compScore<maxScore:
    userChoice = input("Enter your choice:").strip().lower()
    if userChoice not in choices:
        print("Enter a valid choice: ")
        continue
    compChoice = random.choice(choices)
    print("Computer chose: " + compChoice)
    if compChoice==userChoice:
        print("It's a draw")
    elif(userChoice=="rock" and compChoice=="paper") or (userChoice=="scissors" and compChoice=="paper") or (userChoice=="paper" and compChoice=="rock"):
        print("You won this round")
        userScore+=1
    else:
        print("Computer won this round")
        compScore +=1
    print("Your score:" + str(userScore), "Computer score:" + str(compScore))

if userScore == maxScore:
    print("Congratulations! You won the match!")
else:
    print("Computer wins the match.")