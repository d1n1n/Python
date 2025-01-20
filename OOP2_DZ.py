class Airplane():
    def __init__(self,typeA,amountPassangers,maxAmountOfPassengers):
        self.type = typeA
        self.amount = amountPassangers
        self.maxAmount = maxAmountOfPassengers
    
    
    def __eq__(self, other):
        return (self.type == other.type)
    
    def __add__(self,value):
        if value>0:
            
            self.amount += value
            
        else:
            print("CANNOT ADD LESS THAN 0")
        return self.amount
    
    def __sub__(self,value):
        self.amount -= value
        return self.amount
    
    
    def __gt__(self,other):
        return (self.maxAmount >other.maxAmount)
    
    def __lt__(self,other):
        return isinstance(other, Airplane) and self.maxAmount < other.maxAmount
    def __ge__(self,other):
        return (self.maxAmount >=other.maxAmount)
    
    def __le__(self,other):
        return (self.maxAmount <=other.maxAmount)
    
    def __int__(self):
        return int(self.amount)
    
    def __str__(self):
        return f"Type of Airplane: {self.type}"
    
plane1 = Airplane("Boeing 747", 150, 500)
plane2 = Airplane("Boeing 747", 200, 400)
plane3 = Airplane("Airbus A320", 180, 300)


print(plane1<=plane2)