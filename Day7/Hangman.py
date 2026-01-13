import random
word_list = ["goat","dog","human","alcatras"]

word = random.choice(word_list)

won = False

display = "_" * len(word)
lives = 3
print(display)

guesses = set()

while not won:
    guess = input("What is your guess?")
    if guess in guesses:
        print("you already guessed that letter")
        continue
    guesses.add(guess)

    display =""
    for letter in word:
        if letter in guesses:
            display = display + letter
        else:
            display += "_"
    if guess not in word:
        lives -= 1
        print(f"you lost a life. Lives left: {lives}")
    print(display)

    if "_" not in display:
        won = True
        print("YOU WON THE GAME!")
    if lives == 0:
        won = False
        print("GAME OVER")
        break