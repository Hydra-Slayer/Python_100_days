biddings = {}

name = input("Enter your name: ")
bid = int(input("Enter your bid: "))
biddings.update({name : bid})

c = True
while c:
    q = input("Are there any other bidders?")
    if q == "yes":
        c = True
    else:
        break
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    biddings.update({name : bid})
    
for name in biddings:
    if biddings[name] == max(biddings.values()):
        print(f"The winner is {name} with a bid of {biddings[name]}")
        break