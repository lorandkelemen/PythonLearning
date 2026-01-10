import random
import string_utils

letters = ['a','b','c','d','e','f','g','h','i','j','k']
numbers = [1,2,3,4,5,6,7,8,9]
symbols = ['!','@','#','$','%','^','&','*']

nr_of_numbers = int(input("How many numbers do you want?"))
nr_of_letters = int((input("How many letters do you want?")))
nr_of_symbols = int(input("How many symbols do you want?"))

print(type(nr_of_letters))

password = ""
# for number in range(1,nr_of_letters+1):
#
#     password = password + letters[random.randint(0,len(letters)-1)]
#
#
# for number in range(1,nr_of_numbers+1):
#     password = password + str(numbers[random.randint(0,len(numbers)-1)])
#
# for number in range(1,nr_of_symbols+1):
#     password = password + symbols[random.randint(0,len(symbols)-1)]

for number in range(1, nr_of_numbers + 1):
    random_char = str(random.choice(numbers))
    password += random_char
for number in range(1, nr_of_letters + 1):
    random_char = random.choice(letters)
    password += random_char
for number in range(1, nr_of_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char

print(f"your generated password is: {password}")

#hard version - use shuffle
shuffled_pass = string_utils.shuffle(password)
print(f"your hard pass: is: {shuffled_pass}")