import random
pchoice = input("Rock Paper or Scissors")



cchoice = random.randint(1,3)

choices = {
    1 : "Rock",
    2 : "Paper",
    3 : "Scissors"
}

print(f" YOUR CHOICE WAS : {pchoice}")
print(f" COMPUTER's CHOICE WAS : {choices[cchoice]}")
if pchoice.lower() == "rock":
    if cchoice == 1:
        print("its a draw")
    elif cchoice == 2:
        print("you lose")
    else :
        print("you win")

if pchoice.lower() == "paper":
    if cchoice == 1:
        print("you win")
    elif cchoice == 2:
        print("its a draw")
    else :
        print(" you lose")

if pchoice.lower() == "scissors":
    if cchoice == 1:
        print("you lose")
    elif cchoice == 2:
        print("its a win")
    else :
        print(" you draw")
