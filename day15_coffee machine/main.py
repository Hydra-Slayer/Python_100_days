from flavors import MENU, resources
is_on = True

def report():
    print(resources)

def check_res(flavor):
    is_suffice = True
    for ingredient in list(MENU["espresso"]["ingredients"].keys()):
        if resources[ingredient] < MENU[flavor]["ingredients"][ingredient]:
            is_suffice = False
            break
    return is_suffice

def insert_coins(q,d,n,p, cost):
    
    sum = (float(q)*0.25) + (float(n) * 0.05) + (float(d) * 0.1) + (float(p) * 0.01)
    if sum < cost:
        print("Sorry insert more money!")
        return False
    else:
        print(f"Here is the change: {sum-cost}$")
    return True

def make_coffee(flavor):
    no_of_ingredients = len(MENU[flavor]["ingredients"])
    for i in range(no_of_ingredients):
        
        ingredient = list(MENU[flavor]["ingredients"].keys())[i] 
        
        resources[ingredient] -= MENU[flavor]["ingredients"][ingredient]
        
    print(f"Here is your {flavor}. Enjoy!")


def working():
    while is_on:
        choice = input("What would you like to drink?\n1. espresso\n2. latte\n3. cappuccino\n")
        
        #maintainance features
        if choice == "report":
            report()
            continue
        elif choice == "off":
            return
        
        #select flavors
        if choice == "1":
            to_make = "espresso"
            to_pay = MENU[to_make]["cost"]
            if check_res(to_make):
                print(f"Please pay: {to_pay}")
            else:
                print("Not enough resources. Try another flavor!")
                continue
        elif choice == "2":
            to_make = "latte"
            to_pay = MENU[to_make]["cost"]
            if check_res(to_make):
                print(f"Please pay: {to_pay}")
            else:
                print("Not enough resources. Try another flavor!")
                continue
        elif choice == "3":
            to_make = "cappuccino"
            to_pay = MENU[to_make]["cost"]
            if check_res(to_make):
                print(f"Please pay: {to_pay}")
            else:
                print("Not enough resources. Try another flavor!")
                continue
        else:
            print("Enter a valid choice")
        
        quarters = input("How many quarters? ")
        dimes = input("How many dimes? ")
        nickels = input("How many nickels? ")
        pennies = input("How many pennies? ")
        if insert_coins(q = quarters, d = dimes, n = nickels, p = pennies, cost = to_pay):
            make_coffee(to_make)
        else:
            
            print("Please Try again")


if __name__ == "__main__":
    working()