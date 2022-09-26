from art import logo

print(logo)

bids = {}
bidding = False

def highestBidder(records):
    bid = 0
    for bidder in records:
        amount = records[bidder]
        if amount > bid:
            bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ₦{bid}")


while not bidding:
    name = input("What is your name?\n")
    price = int(input("What is your bid? ₦"))
    bids[name] = price
    otherBidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if otherBidders == "no":
        bidding = True
        highestBidder(bids)
        print("Thank you for using  our platform....")
    elif otherBidders == "yes":
        continue



