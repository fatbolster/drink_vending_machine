class VendingMachine:
    def __init__(self):
        self.resources = {
                "water": 500,
                "syrup": 300
            }
        
    def report (self):
        for item, amount in self.resources.items():
            print (f"{item}: {amount:.2f}ml")

    def is_resources_sufficient(self, can):
        enough = True 
        for item in can.ingredients:
            if self.resources[item] < can.ingredients[item]:
                print (f"There is not enough {item}")
                enough = False 
        return enough 
    
    def dispense_drink(self,order):
        for item in order.ingredients: 
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Thank you for purchasing!")

    