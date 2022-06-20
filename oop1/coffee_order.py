class CoffeeOder:
    menu_type = 'Coffee' #class variables
    total = 0

    def __init__(self,customer_name:str,menu:str,num:int=1,size:str='R') -> None: #instance varibles 
        self.customer_name = customer_name
        self.menu = menu.upper()
        self.num = num
        self.size = size.upper()
        self.price = 0 #กำหนด price ไว้ก่อนหรือไม่ต้องก็ได้

    def check_menu(self):
        menu_dictionary = {
            'CM' :5.99,
            'CP' :4.99,
            'AM' :4.99,
            'CL' :4.99,
            'VL' :4.75,
            'ES' :3.00
            }

        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)
    
    def compute_price(self):
        if self.size == 'L':
            #
            self.price += 1
        elif self.size == 'XL':
            self.price += 1.5
        else:
            self.price

        #คำนวณราคารวม = จำนวนแก้ว * ราคา
        #total = num * price
        CoffeeOder.total = self.num * self.price
    
    def display_detail(self):
        self.check_menu
        return f'{self.customer_name},{self.menu},{self.size} * ${self.price} => ${CoffeeOder.total}' 

    def __del__(self):
        print("object was destroyed")

if __name__ == "__main__" :
    order1 = CoffeeOder('John','es')
    order2 = CoffeeOder('Mary','am',2,'l') 

    order1.check_menu()
    order1.compute_price()
    print(order1.display_detail())

    order2.check_menu()
    order2.compute_price()
    print(order2.display_detail())