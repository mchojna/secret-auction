"""
Title: Secret Auction
Author: Michał Chojna
Date: 09.06.2022
Description: Users place bids on the on item, without knowing each other bids
"""

# Imports modules
import os
import art

# Boolean initializes program
program = True

# While loop initializes program
while program:

    # Cleans the window
    os.system("clear")

    # Prints welcome logo
    print(art.logo)

    # Prints welcome message
    print("Welcome to the secret auction program.")

    # Creates dictionary for bidder's name and bidder's bid
    auction_dict = {}

    # Boolean initializes Secret Auction
    auction = True

    # While loop initializes Secret Auction
    while auction:

        # Takes bidder's name
        name = input("What is your name? ")

        # Takes bidder's bid
        bid = int(input("What is  your bid? $"))

        # Adds to the dictionary bidder's name and bidder's bid
        auction_dict[name] = bid

        # While loop to check if there are other bidders
        while True:

            # Takes answer to the question if there are any other bidders
            again = input("Are there any other bidders? Type 'yes' or 'no'. ")

            # Checks if the user's answer if there are any other bidders is correct
            if again.lower() == "yes" or again.lower() == "no":
                break

        # Cleans the window
        os.system("clear")

        # Checks if the answer to the question if there are any other bidder is no
        if again.lower() == "no":

            # If the answer to the question if there are any other bidders is no
            # Closes auction
            auction = False

    # Creates a string to hold the best bidder's name
    winner_name = ""

    # Creates an integer to hold the best bidder's bid
    winner_bid = 0

    # For loop iterates through names of the bidders
    for name in auction_dict:

        # Checks if the actual bidder's bid is bigger than general best bidder's bid
        if auction_dict[name] > winner_bid:

            # If actual bid is bigger than general best bid
            # Changes the name of the general best bidder's name to the actual best bidder's name
            winner_name = name

            # Changes the name of the general best bidder's bid to the actual best bidder's bid
            winner_bid = auction_dict[name]

    # Prints the best bidder's name and the best bidder's bid
    print(f"The winner is {winner_name} with a bid of ${winner_bid}.")

    # While loop to check if the user wants to one more time use program
    while True:

        # Takes the user's decision to run the program again is correct
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")

        # Check if the user's decision to run the program again is correct
        if again.lower() == "yes" or again.lower() == "no":

            # If user's decision to run the program again is correct
            # Breaks the loop
            break

    # Checks if  user's decision to run again the program is no
    if again.lower() == "no":

        # If user's decision to run again the program is no
        # Breaks the loop
        break
