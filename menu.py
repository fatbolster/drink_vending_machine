class DrinkMenu:
    def __init__(self, name, water, syrup, cost): 
        self.name = name 
        self.cost = cost 
        self.ingredients = {
            "water" : water, 
            "syrup" : syrup
        }

class Drink: 
    def __init__(self):
        self.menu = [
            DrinkMenu(name = "Coca-Cola", cost = 1.00, water = 100, syrup = 50),
            DrinkMenu(name = "Sprite", cost = 0.90, water = 80, syrup = 40),
            DrinkMenu(name = "Fanta Grape", cost = 1.10, water = 90, syrup = 60),
            DrinkMenu(name = "Ice Lemon Tea", cost = 1.10, water = 80, syrup = 40),
            DrinkMenu(name = "Root Beer", cost = 1.30, water = 90, syrup = 60 )
        ]
    
    def get_drink(self):
        list = ""
        for item in self.menu: 
            list += f"{item.name}/"
        return list
    
    def find_drink (self, drink):
        for item in self.menu:
            if item.name == drink:
                return item 
            else: 
                pass  
        print ("Sorry! That item is unavailiable")
