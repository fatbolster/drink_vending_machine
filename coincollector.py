class CoinCollector():
    def __init__ (self):
        self.currency = "S$"
        self.quantity = {
            "10 cents coins": 0.10,
            "20 cents coins": 0.20,
            "50 cents coins": 0.50,
            "dollar coins": 1.00
        }
        self.earnings = 0 
        self.moneyslot = 0 

    def report(self):
        print (f"Earnings: S${self.earnings:.2f}")
    
    def process_coin(self):
        for coin,value in self.quantity.items():
            while True:
                try:
                    number = int(input((f"How many {coin} do you have? ")))
                    if number > 0:
                        self.moneyslot += value * number
                        break
                    else:
                        print ("Please input a non-negative integer value")
                except ValueError: 
                    print("Please input a valid numerical Value")

    def make_payment(self, cost):
        if self.moneyslot > cost:
            change = self.moneyslot - cost
            self.earnings += cost 
            print (f"Here is {self.currency}{f"{change:.2f}"}. Thank you!")
            self.moneyslot = 0 
            return True 
        else: 
            print ("Not enough money. Money returned！")
            self.moneyslot = 0
            return False 


