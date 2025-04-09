
report_machine = {
    "Water" : 300,
    "Milk" : 200 ,
    "Coffee":100,
    "Money": 0,
}
espresso = {
    "Water": 50,
    "Milk": 0,
    "Coffee": 18,
    "Money": 1.50,
}

LATTE = {
    "Water": 200,
    "Milk": 150,
    "Coffee": 24,
    "Money": 2.50,
}

CAPPUCCINO = {
    "Water": 250,
    "Milk": 100,
    "Coffee": 24,
    "Money": 3.00,
}
QUARTER = 0.01
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.25
def report():
    return report_machine

def enter_money(num_quarter , num_dimes ,num_pennies , num_nickles ):
    sum = 0
    sum = (QUARTER * num_quarter) + (DIMES * num_dimes) + (NICKLES * num_nickles) + (PENNIES * num_pennies)
    return sum
def ressource_machine():
    for key in report_machine:
        if key == "Money":
            continue
        elif report_machine[key] < espresso[key] or report_machine[key] < LATTE[key] or report_machine[key] < CAPPUCCINO[key]:
            return False
        else:
            return True
def choix_espresso():
    for key in report_machine:
        if key == "Money":
            continue
        report_machine[key]=report_machine[key] - espresso[key]
    return report_machine

def choix_latte():
    for key in report_machine:
        if key == "Money":
            continue
        report_machine[key]=report_machine[key] - LATTE[key]
    return report_machine

def choix_cappuccino():
    for key in report_machine:
        if key == "Money":
            continue
        report_machine[key]=report_machine[key] - CAPPUCCINO[key]
    return report_machine


def change_espresso(num_quarter , num_dimes ,num_pennies , num_nickles ):
    if enter_money(num_quarter , num_dimes ,num_pennies , num_nickles ) == espresso["Money"]:
        return "No change "
    elif espresso["Money"] >= enter_money(num_quarter , num_dimes ,num_pennies , num_nickles ):
        return "You don't have enough money "
    else:
        return f"Here is {round(enter_money(num_quarter , num_dimes ,num_pennies , num_nickles) - espresso["Money"],2)} in change"

def change_latte(num_quarter , num_dimes ,num_pennies , num_nickles ):
    if enter_money(num_quarter , num_dimes ,num_pennies , num_nickles ) == LATTE["Money"]:
        return "No change "
    elif LATTE["Money"] >= enter_money(num_quarter , num_dimes ,num_pennies , num_nickles ):
        return "You don't have enough money"
    else:
        return f"Here is {round(enter_money(num_quarter , num_dimes ,num_pennies , num_nickles) - LATTE["Money"],2)} in change"


def change_cappuccino(num_quarter , num_dimes ,num_pennies , num_nickles ):
    if enter_money(num_quarter , num_dimes ,num_pennies , num_nickles ) == CAPPUCCINO["Money"]:
        return "No change "
    elif CAPPUCCINO["Money"] >= enter_money(num_quarter , num_dimes ,num_pennies , num_nickles ):
        return "You don't have enough money"
    else:
        return f"Here is {round(enter_money(num_quarter , num_dimes ,num_pennies , num_nickles) - CAPPUCCINO["Money"],2)} in change"



while True:
    choix = input("What would you like? (espresso, latte, cappuccino): ")
    print("Please insert coins")
    quarter =int(input("Enter number of quarters: "))
    dimes =int(input("Enter number of dimes: "))
    nickles =int(input("Enter number of nickles: "))
    pennies =int(input("Enter number of pennies: "))
    if ressource_machine() == False:
        break
    if choix == "espresso":
        choix_espresso()
        print(round(enter_money(quarter , dimes ,pennies ,nickles),2))
        print(change_espresso(quarter , dimes ,pennies ,nickles))
        report_machine["Money"]+= espresso["Money"]
        print("Here is you espresso \u2615 ")

    elif choix == "latte":
        choix_latte()
        print(round(enter_money(quarter , dimes ,pennies ,nickles),2))
        print(change_latte(quarter , dimes ,pennies ,nickles))
        report_machine["Money"]+=LATTE["Money"]
        print("Here is you latte \u2615")

    elif choix == "cappuccino":
        choix_cappuccino()
        print(round(enter_money(quarter , dimes ,pennies ,nickles),2))
        print(change_cappuccino(quarter , dimes ,pennies ,nickles))
        report_machine["Money"]+= CAPPUCCINO["Money"]
        print("Here is you cappuccino \u2615")

    print(report())

print("You need to refill the machine ☕🔄")