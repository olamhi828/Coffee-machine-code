from Data import coffee_file,resources,profit

is_on=True
def is_sufficient(user):
    for item in user:
        if user[item] >= resources[item]:
            print(f"Sorry, There is not enough ({item})")
            return False
        else:
            return True
def process_coins():
    print("Please insert coins")
    total=int(input("how many quarters "))*0.25
    total+=int(input("how many dimes "))*0.1
    total+=int(input("how many nickles "))*0.05
    total+=int(input("how many pennies "))*0.01
    return total

def transaction_successful(money_received,drink_price):
    global profit
    if money_received>=drink_price:
        change=round(money_received-drink_price,2)
        print(f"Here is ${change} change in dollars")
        profit+=drink_price
        return True
    else :
        print("Sorry, that is not enough money! Money refunded")
        return False
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"Here is your {drink_name} .Enjoy!😘😎")
while is_on:
    for a, dict in enumerate(coffee_file):
        print(f"{chr(65 + a)} : {dict}")
    user_choice=input("What would you like to take? Type 'off' to turn off the machine or 'report' to check the current status  ").title().strip()
    if user_choice=="off".title():
        is_on=False
    elif user_choice=="report".title():
       print(f"water :{resources["water"]}ml")
       print(f"Milk : {resources["milk"]}ml")
       print(f"coffee {resources["coffee"]}g")
       print(f"profit :${profit}")
    else:
        
        drink=coffee_file[user_choice.title()]
        if is_sufficient(drink["ingredients"]):
           
            payment=process_coins()
            if transaction_successful(payment,drink["cost"]):
                make_coffee(user_choice,drink["ingredients"])









        