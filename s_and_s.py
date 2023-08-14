import datetime
def sort_by_order_date(pizza_order):
    pizza_order.sort(key=lambda order_date: datetime.datetime.strptime(order_date, '%Y-%m-%d'))

def sort_by_amount(pizza_order):
    for i in range(len(pizza_order) - 1): #iterating n-1 times
        minimum = i 
        for j in range(i + 1, len(pizza_order)): # Compare i+1 and i
            if(pizza_order[j] < pizza_order[minimum]):
                minimum = j
        if (minimum != i):
            pizza_order[i], pizza_order[minimum] = pizza_order[minimum], pizza_order[i]
    return pizza_order


def search_by_customer(customer,pizza_order):

    p = 0 
    global iterations
    i = 0 
    while p < len(pizza_order):
        i += 1
        if customer == pizza_order[p]:
            return "Customer is found."
        p += 1 
    return "Customer is not found."

def search_by_order_date(date, pizza_order):
    for order in pizza_order:
        if order.order_date == date:
            return order
    return "Order date is not found."
        

def order_before_date(date, pizza_order):
    pizza_order = pizza_order.sort(key=lambda order_date: datetime.strptime(order_date, '%d-%b-%y'))
    for i in range(len(pizza_order)):
        if pizza_order[i].order_date < date:
            return pizza_order[:i]
    return "The input order date is the earliest one on the record."


def order_after_date(date, pizza_order):

    pizza_order = pizza_order.sort(key=lambda order_date: datetime.strptime(order_date, '%d-%b-%y'))
    for i in range(len(pizza_order)):
        if pizza_order[i].order_date > date:
            return pizza_order[i:]
    return "The input order date is the lastest one on the record."