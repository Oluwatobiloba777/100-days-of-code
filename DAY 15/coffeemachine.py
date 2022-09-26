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

profit = 0

def checkResource(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True

def processCoins():
    print('Please insert coins.')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.1
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total

def checkTransaction(money,drink):
    global profit
    if money >= drink:
        change = round(money - drink, 2)
        print(f"Here is ${change} in change.")
        profit += drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def makeCoffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")


while True:
    choice = input("What would you like? (espresso/latte/cappuccino)....If you are done then type 'off': ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if checkResource(drink["ingredients"]):
            payment = processCoins()
            if checkResource(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])