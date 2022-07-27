from art import logo
from data import alphabet

def auction(name, bid):
    next = "yes"
    while next == "yes":
        bids[name] = int(bid)
        next = input("Is there someone else to bid? yes/no\n")
        if next == "no":
            break
        else:
            clear()
        name = input("Enter your name: ")
        bid = int(input("What's your bid?: $"))
    return bids

def check_value(bids_dict):
    max_value = 0
    winner = ""
    for key in bids:
        value = bids[key]
        if value > max_value:
            max_value = value
            winner = key      
    return "The highest bid: " + str(max_value) + f". The winner is {winner.title()}"

def is_name_correct(text):
    while text.isalpha() == False:
        text = input("Enter your name: ")
        continue
    return text

def is_bid_correct(number):
    while number.isnumeric() == False:
        number = input("What's your bid: $")
        continue
    return int(number)   
   
clear = lambda: system("clear")   
            
print(logo)
name = input("Enter your name: ")
is_name_correct(name)
bid = input("What's your bid?: $")
is_bid_correct(bid)
bids = {} # {name:bid, name:bid}

auction(name, bid)
print(bids)
print(check_value(bids))
        
