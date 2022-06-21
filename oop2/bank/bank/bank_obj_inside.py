#this file inside
#
from customer import Customer
from account import Accout

cus1 = Customer()
cus1.new_customer()

cus1_acc = Accout()
cus1_acc.open_account(cus1.name,"Saving",'1150-1112',500)

print("**** Open Bank Account Detail ****")
print(cus1.cus_info())
print(cus1_acc.display_balance())