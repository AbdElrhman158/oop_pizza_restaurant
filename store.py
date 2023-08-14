from s_and_s import *
class Store():
    def __init__(self, employees, address, teln, sale, name):
        self.employees = []
        self.address = address
        self.tel_num = str(teln)
        self.sale = []
        self.num_served = 0
        self.name = name

    
    def add_emp(self,employees):
        self.employees.append(employees)
    
    def rm_emp(self,employees):

        self.employees.remove(employees)
    
    def set_address(self,address, zip_code):

        self.address = str(address)
        self.zip_code = int(zip_code)
    
    def get_monthly_sale(self):

        sort_by_order_date(self.sale)
        month = self.sale[0].orderd.month
        while len(self.sale) > 0:
            amount = 0 
            i = 0
            while self.sale[i].orderd.month == month:
                if i < len(self.sale):
                    amount += self.sale[i].amount
                    i += 1
            print('The monthly sale for',month, 'is',amount,'.')
    
    def describe_store(self):
        intro = self.name + " serves delicious " + self.crut + " pizza. "
        print("\n" + intro)
    
    def set_num_served(self, num_served):
        self.num_served = num_served

    def increment_num_served(self, add_served):
        self.num_served += add_served