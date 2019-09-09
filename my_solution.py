#Importing the json module
import json
#import from random module so we can have a random sequence of donut ingredients 
from random import choice as randchoice

#Assigning files to variables so they can be easily accessed and called
DONUTS_FILE = "./donuts.json"
MONEY_FIlE = "./transactions.txt"

#Load function so we can easily get the data we need from the file
def load(filename):
    with open(filename) as store_file:
        donut_json = json.load(store_file)
    #Doing this lets us easily use the items in the dictionaries 
    toppings = donut_json.get("toppings")
    flavors = donut_json.get("flavors")
    return toppings, flavors

#Input validation for choices 
def get_choice(options):
    while True:
        choice = input(">>> ")
        if choice in options:
            return choice
        else:
            print(f"Sorry {choice} is not an option")

#this function was made so we can easily append the data to the transaction file
def save_transaction(name, topping, flavor, cash, change):
    return '{}, {}, {}, {}, {}'.format(name, topping, flavor, cash, change)

def main():
    #Tuple assigning this allows us to easily pull dictionary items from the json file
    toppings, flavors = load(DONUTS_FILE)
    print("""Hello! Welcome to the Donut Shop!
    \tAll donuts are 75c, cash only.")
    \tChoose your topping and flavor! Or get a random flavor!")
    \nCan we get a name for this order?""")
    name = input(">>> ")
    print(f"Welcome {name}! We are happy to assist you today!")
    print("[1] custom make your donut? or [2] have a random combination?")
    choice = get_choice(["1", "2"])
    if choice == "1":
        print("What topping would you like?")
        print(" | ".join(toppings))
        topping = get_choice(toppings)
        print("What flavor would you like?")
        print(" | ".join(flavors))
        flavor = get_choice(flavors)
        print(
            f"Your order: donut with {topping} topping and {flavor} flavored icing, great choice!"
        )
    else:
        topping = randchoice(toppings)
        flavor = randchoice(flavors)
        print(
            f"Your order: donut with {topping} topping and {flavor} flavored icing, great choice!"
        )

    print(
        """ 
    >>> Your total is 0.75
    >>> How much are you paying with?"""
    )
    print(" ")
    cash = float(input(">>>"))
    change = cash - 0.75
    print("Here is your change: ${:.2f}\nHave a great day!".format(change))

    ledger = save_transaction(name, topping, flavor, cash, change)

    with open(MONEY_FIlE, "a") as transaction_file:
        transaction_file.write(ledger)

if __name__ == "__main__":
    main()
