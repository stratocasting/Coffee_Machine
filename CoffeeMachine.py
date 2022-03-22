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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# quarters= 0,25
# dimes = 0,10
# nickles = 0,5
# pennies = 0,1


def is_resources_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print (f"sorry there is no enough {item}")
            return False
    return True


def is_money_sufficient(order_cost):
    quarters = 0.25 * int(input("how many quarters?: "))
    dimes = 0.10 * int(input("how many dimes?: "))
    nickles = 0.5 * int(input("how many nickles?: "))
    pennies = 0.1 * int(input("how many pennies?: "))
    total_money = quarters + dimes + nickles + pennies
    if MENU[choice]["cost"] > total_money:
        print("no enough coins")
    else:
        print(f"your change is {total_money - MENU[choice]['cost']}")





is_on = True


while is_on:
    choice = input("What would yo like?: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Milk: {resources['milk']}")
        print(f"Water: {resources['water']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = (MENU[choice])
        if is_resources_sufficient(drink["ingredients"]):
            print ("please insert coin")
            is_money_sufficient(drink["cost"])
            resources["water"] -= drink["ingredients"]["water"]
            resources["coffee"] -= drink["ingredients"]["coffee"]
            if drink == "latte" or drink == "cappuccino":
                resources["milk"] -= drink["ingredients"]["milk"]

