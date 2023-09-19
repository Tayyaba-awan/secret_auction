import art
print(art.logo)
print("This is a blind auction, you can input your name and bid.")
print(
    "After that, pass the computer to other person and find who's the highest bidder!"
)
bids={}
should_continue=False
# create a lop that will store user inputs
while not should_continue:
    name=input("what is your name?\n")
    bid=int(input("type the price of bid: \n$"))
    bids[name]=bid
    def find_bidder(bidding_record):
        highest_bid=0
        winner=""
        # check if the current user bid is the highest
    # print the result if the user type "no" to repeat
        for bidder in bidding_record:
            bidder_amount=bidding_record[bidder]
            if  bidder_amount>highest_bid:
                highest_bid=bidder_amount
                winner=bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")
    # ask the user to repeat
    other_user=input("Are there any other bidders? Type 'yes or 'no'.\n")
    if other_user=="no":
        should_continue=True
        find_bidder(bids)
        
    