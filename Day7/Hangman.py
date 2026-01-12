import random
world_list = ["goat","dog","human"]

lives = 5

#print(random.choice(world_list))
word = random.choice(world_list)
word_length = len(word)
display = ""
for letter in word:
    display += "_"
print(f"your word is {display} \n")

guess = input("Guess a letter: ").lower()

display = ""
for char in word:
    if guess == char:
        display +=char
    else:
        display +="_"

print(display)

#todo
#ask user to input letter

#todo 2
#check if in word, if yes x if no y