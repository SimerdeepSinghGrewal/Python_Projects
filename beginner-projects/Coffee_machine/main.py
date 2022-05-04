MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
FAULT= True
MONEY= 0
enough_money= True
def coin_calc():
    print("Please insert coins.")
    quater = int(input("How many quaters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penni = int(input("How many pennies?: "))
    total_amount = (quater * 0.25) + (dime* 0.10) + (nickle * 0.05) + (penni * 0.01)
    #print (type(total_amount))
    return total_amount

def bill_calc(user_money, user_choice):
    if user_choice == "espresso":
        price = MENU[user_choice]["cost"]
    elif user_choice == "latte":
        price = MENU[user_choice]["cost"]
    elif user_choice == "cappuccino":
        price = MENU[user_choice]["cost"]
    if user_money < price:
        print("Sorry that's not enough money. Money refunded. ")
        global enough_money
        enough_money = False
    else:
        change = user_money - price
        global MONEY
        MONEY += price
        print (f"Here is ${change: .2f} dollars in change.")


def make_coffee(user_choice):
    req_water = MENU[user_choice]["ingredients"]["water"]
    req_milk = MENU[user_choice]["ingredients"]["milk"]
    req_coffee = MENU[user_choice]["ingredients"]["coffee"]
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if req_water > resources["water"]:
            print (f"Sorry there is not enough water.\n Here is your ${user_money: .2f} refund.")
            global FAULT
            FAULT = False
        elif req_milk > resources["milk"]:
            print (f"Sorry there is not enough milk.\n Here is your ${user_money: .2f} refund.")
            FAULT = False
        elif req_coffee > resources["coffee"]:
            print (f"Sorry there is not enough coffee.\n Here is your ${user_money: .2f} refund.")
            FAULT = False
        elif enough_money:
            resources["water"] -= req_water
            resources["milk"] -= req_milk
            resources["coffee"] -= req_coffee
            print (f"Here is your {user_choice} ☕ enjoy. ")


more_coffee = True
while more_coffee:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        user_money= coin_calc()
        make_coffee(user_choice)
        if FAULT:
            bill_calc(user_money, user_choice)

    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${MONEY}")
    elif user_choice == "off":
        more_coffee = False
