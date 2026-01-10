scores = [1,4,8]
#print(max(scores))

maxscore = 0
for score in scores:
    if score > maxscore:
        maxscore = score


print(maxscore)
####################################
#gauss challenge

totalsum = 0
for number in range(1,101):
    totalsum = totalsum + number
print(totalsum)
####################################
# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# e.g. it might start off like this:
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc
##########################
fizz = "Fizz"
buzz = "Buzz"
fizzbuzz = "FizzBuzz"

for nr in range(1,101):
    if nr % 3 == 0 and nr % 5 == 0:
        print(fizzbuzz)
    else:
        if nr % 3 == 0:
            print(fizz)
        else:
            if nr % 5 == 0:
                print(buzz)
            else:
                print(nr)


