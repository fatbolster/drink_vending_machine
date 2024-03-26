from vendingmachine import VendingMachine 
from coincollector import CoinCollector 
from menu import Drink

machine = VendingMachine()
coin = CoinCollector() 
drink = Drink() 
status = True

while status == True:
    options = drink.get_drink()
    user = input (f"What drink would you like to order? {options}")
    order = drink.find_drink(user)
    if user == "report":
        machine.report()
        coin.report()
    elif user == "off":
        print ("Offing Machine")
        status = False 
    if order:
        cost = order.cost
        if machine.is_resources_sufficient(order) == True:
            coin.process_coin()
            if coin.make_payment(cost):
                machine.dispense_drink(order)
    else:
        pass 
    

