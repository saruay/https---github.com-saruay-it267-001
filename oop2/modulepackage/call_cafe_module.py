import imp
from cafe import Dessert,Drink
dessert_menu = Dessert()
print(dessert_menu.show_dessrt())

#แสดงรายการเครื่องดื่มของร้าน
drink_menu = Drink()
print(drink_menu.show_drink())

#เพิ่มรายการเครื่องดื่ม
drink_menu.add_drink('juice')
drink_menu.add_drink('smoothy')
print(drink_menu.show_drink())