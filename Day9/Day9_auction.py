print(r"""
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
""")

print("welcome to the secret auction! >:)")

players_bids = {}

def game_loop():
    winner = ""
    name = input("What is your name?")
    bid = int(input("What is your bid? $:"))

    players_bids.update({name: bid})

    more_players = (input("Are there any other bidders? Type 'yes' or 'no':"))

    if more_players == "yes":
        game_loop()
    elif more_players == "no" :
        winner_name = max(players_bids, key=players_bids.get)

        print(f"{winner_name} has won the auction!")

game_loop()