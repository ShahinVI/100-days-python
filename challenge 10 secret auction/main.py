from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

bidders={}

print(logo)
print("Welcome to the secret auction program.")
bid = input("do you want to bid? y/n ")
auction=True

max_bid=0
max_name=""

while auction:
    if bid.lower() == "y" or bid.lower() == "yes":
        clear()
        print(logo)
        name = input("What is your name? ")
        bid_amount = int(input("How much do you want to bid? "))
        bidders[name] = bid_amount
        bid = input("is there another bidder? y/n ")
    elif bid.lower() == "n" or bid.lower() == "no":
        auction = False
        if not bidders == {}:
            for key, value in bidders.items():
                if max_bid <= value:
                    max_bid = value
                    max_name = key
            clear()
            print(logo)
            print(f"The winner is {max_name} with a bid of ${max_bid}.")
        else:
            print("no one placed a bid. ")
    else:
        clear()
        print(logo)
        print("you wrote an invalid value. try again. ")
        bid = input("is there another bidder? y/n ")


