import os
from art import logo



def result(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        amount = bids[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

clear = lambda: os.system('cls')
print(logo)
auction = {}
auction_end = True
while auction_end:
    person = input("What is yout name ?: ")
    bid = int(input("What's your bid ?: $"))
    auction[person] = bid
    auction_again = input("Are there any other bidders ? Type 'yes' or 'no'.\n")
    clear()
    if auction_again == "no":
        auction_end = False
        result(auction)
        # for bids in auction:
        #   auction[bids]
