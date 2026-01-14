# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
#
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# 2. Then check for the number of times the letters in the word LOVE occurs.
#
# 3. Then combine these numbers to make a 2 digit number and print it out.



def calculate_love_score():
    word1 = "TRUE"
    word2 = "LOVE"

    first_name = (input("Enter the first name: ")).lower()
    second_name = (input("Enter the second name: ")).lower()

    combined_words = (word1 + word2).lower()
    combined_names = first_name + second_name

    total_score = 0
    for w_letter in combined_words:
        for n_letter in combined_names:
            if w_letter == n_letter:
                total_score += 1

    print(f"your love score is {total_score}")

calculate_love_score()
