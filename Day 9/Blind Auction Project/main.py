# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

print("Welcome to the secret auction program.\n")
other_bidders = "yes"
bid_dictionary={}

while other_bidders=="yes":
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_dictionary[name]=bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n"*100)


def find_highest():
    max_bid = 0
    max_key = ""
    for key in bid_dictionary:
        if bid_dictionary[key] > max_bid:
            max_bid = bid_dictionary[key]
            max_key = key
    print(f"The winner is {max_key} with a bid of ${bid_dictionary[max_key]}")


find_highest()