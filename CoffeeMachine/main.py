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

program_off = False
given_money = 0.0
machine_total_money = 0.0


# TODO 1 Print Report Function

def Print_Report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {machine_total_money}")


# TODO 2 Check Resources Function boolean
def Check_Resources(coffe_type):
    if coffe_type == "espresso":
        if resources['water'] > MENU["espresso"]["ingredients"]["water"]:
                if resources['coffee'] > MENU["espresso"]["ingredients"]["coffee"]:
                    return "1"
                else:
                    return "not enough coffee"
        else:
            return "not enough water"
    elif coffe_type == "latte":
        if resources['water'] > MENU["latte"]["ingredients"]["water"]:
            if resources['milk'] > MENU["latte"]["ingredients"]["milk"]:
                if resources['coffee'] > MENU["latte"]["ingredients"]["coffee"]:
                    return "1"
                else:
                    return "not enough coffee"
            else:
                return "not enough milk"
        else:
            return "not enough water"
    elif coffe_type == "cappuccino":
        if resources['water'] > MENU["cappuccino"]["ingredients"]["water"]:
            if resources['milk'] > MENU["cappuccino"]["ingredients"]["milk"]:
                if resources['coffee'] > MENU["cappuccino"]["ingredients"]["coffee"]:
                    return "1"
                else:
                    return "not enough coffee"
            else:
                return "not enough milk"
        else:
            return "not enough water"

def Check_Money(money,coffe_type):
    if coffe_type == "espresso":
        if money > MENU["espresso"]["cost"]:
            return True
        else:
            return False
    elif coffe_type == "latte":
        if money > MENU["latte"]["cost"]:
            return True
        else:
            return False
    elif coffe_type == "cappuccino":
        if money > MENU["cappuccino"]["cost"]:
            return True
        else:
            return False

# TODO 3 Process Coins Function
def Process_Coins(quarters,dimes,nickles,pennies):
    return 0.25*quarters+0.10*dimes+0.05*nickles+0.01*pennies

# TODO 4 Transaction Check Function

# TODO 5 Make Coffee Function
def Make_Coffee(coffe_type,given_money):
    if coffe_type == "espresso":
        resources['coffee']-=MENU['espresso']['ingredients']['coffee']
        resources['water']-=MENU['espresso']['ingredients']['water']
        given_money-=MENU['espresso']['cost']
        print("Here is your espresso. Enjoy!")
    elif coffe_type == "latte":
        resources['coffee']-=MENU['latte']['ingredients']['coffee']
        resources['water']-=MENU['latte']['ingredients']['water']
        resources['milk']-=MENU['latte']['ingredients']['milk']
        given_money-=MENU['latte']['cost']
        print("Here is your latte. Enjoy!")
    elif coffe_type == "cappuccino":
        resources['coffee']-=MENU['cappuccino']['ingredients']['coffee']
        resources['water']-=MENU['cappuccino']['ingredients']['water']
        resources['milk']-=MENU['cappuccino']['ingredients']['milk']
        given_money-=MENU['cappuccino']['cost']
        print("Here is your cappuccino. Enjoy!")

def coin_insert():
    print("Please insert coin.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    given_money = Process_Coins(quarters, dimes, nickles, pennies)
    return given_money



while not program_off:
    answer = input("What would you like? (espresso/latte/cappuccino):")

    if answer == "espresso":
        resources_sufficient = Check_Resources("espresso")
        if resources_sufficient == "1":
            given_money=coin_insert()
            money_sufficient = Check_Money(given_money, answer)
            if money_sufficient:
                Make_Coffee("espresso",given_money)
                machine_total_money += MENU['espresso']['cost']
                if given_money>0:
                    print(f"Here is ${given_money} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is {resources_sufficient}.")
    elif answer == "latte":
        resources_sufficient = Check_Resources("latte")
        if resources_sufficient == "1":
            given_money = coin_insert()
            money_sufficient = Check_Money(given_money, answer)
            if money_sufficient:
                Make_Coffee("latte",given_money)
                machine_total_money += MENU['latte']['cost']
                if given_money > 0:
                    print(f"Here is ${given_money} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is {resources_sufficient}.")
    elif answer == "cappuccino":
        resources_sufficient = Check_Resources("cappuccino")
        if resources_sufficient == "1":
            given_money = coin_insert()
            money_sufficient = Check_Money(given_money, answer)
            if money_sufficient:
                Make_Coffee("cappuccino",given_money)
                machine_total_money += MENU['cappuccino']['cost']
                if given_money > 0:
                    print(f"Here is ${given_money} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is {resources_sufficient}.")
    elif answer == "report":
        Print_Report()
    elif answer == "off":
        program_off = True
