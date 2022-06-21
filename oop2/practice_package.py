from cusorder.customer import Customer
from cusorder.order import Order

#create object customer
cus1 = Customer("Jame","Nontaburi")

#create object order
order1 = Order("15-06-2022","packed")

#display info
print(f'Order of {cus1.name} on {order1.status} is {order1.status}')