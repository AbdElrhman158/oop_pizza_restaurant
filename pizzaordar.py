from enum import Enum
class ord(Enum):
    ordar_c = 0
    ordar_cr = 1
    ordar_r = 2
    ordar_o_d = 3
    ordar_com = 4

class amountE(Exception):
    pass

class pizzaordar():
    def __init__(self , pizza , store , proc , customer , orderd , amount):
        self.pizza =[]
        self.store = store
        self.proc = proc
        self.customer = customer
        self.orderd = orderd
        self.amount = int(amount)

        if amount<0:
            raise amountE("Error.")
        else:
            self.amount = amount

    def addpizza(self,pizza):
        self.pizza.append(pizza)
    
    def rmpizza(self,pizza):
        self.pizza.remove(pizza)
    
    def geta (self,amount):
        return float(self.amount)
    
    def sets (self,store):
        self.store = store

    def setproc (self,proc):
        self.proc = proc
    
    def orders (self,ords):
        self.ords = ords

    def customer(self,customer):
        self.customer = customer
    
    def ser_o_d(self,orderd):
        self. orderd = orderd
    
    def get_o_d(self,orderd):
        return self.orderd
    
    def __str__(self):
        order_str = """ 
            Amount:{amount}
            Store:{store}
            Customer:{costomer}
            OrderDate:{ordard}
            PorCode:{proc}""".format(amount=self.amount,store=self.store,customer=self.customer,
                                     orderd=self.orderd,proc=self.proc
                                     )
        return order_str