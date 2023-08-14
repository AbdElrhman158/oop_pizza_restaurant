from pizzaordar import *
class crust_type(Enum):
    thin = 0
    thick = 1

class Pizza():
    def __init__(self, toppings, cost):
        self.toppings = []
        self.cost = cost
        self.sold = False
        self.__discount = None
        self.__price = 20

    def addt(self,toppings):
        self.toppings.append(toppings)
    
    def rmt(self,toppings):
        self.toppings.remove(toppings)
    
    def setdis(self,value):
        self.__discount = value
    
    def getp(self):
        if self.__discount is None:
            return self.__price
        else:
            return self.__price * (1 - self.__discount)
    
    def updatep(self, newp):
        if self.sold:
            raise ("We can't update the sale price of this pizza since it's been sold.")
        self.price = newp
    def sale_r(self):
        self.sold = True
        profit = self.price - self.cost
        print('The profit of this order is:', profit)
    
    def crust_type(self,crut):
        self.crut = crut
        
    def __repr__(self):
        return f"Toppings:{self.toppings()}, Price: {self.price()}, Profit:{self.profit()}, Crusty Type: {self.CrustyType()}"

    def __str__(self):
        pizza_str = """
            PizzaToppings:{toppings}
            Cost: {cost} 
            Customer: {customer}
            OrderDate: {orderd}""".format(toppings = self.topppings,
                                              cost = self.cost)
        return pizza_str