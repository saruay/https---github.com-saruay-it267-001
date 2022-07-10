class JuiceOrder:
    menu_type = "Juice"
    total = 0

    def __init__(self,menu:str,size:str='R',price:int=0) -> None:
        self.menu = menu
        self.size = size
        self.price = price

    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30
        }

        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == 'R':
            self.price == 0
        elif self.size == 'L':
            self.price += 5
        else:
            self.price

        JuiceOrder.total = self.price

    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f'{self.menu}({self.size}*{self.price}) => {JuiceOrder.total} baht'

if __name__== "__main__":
    order1 = JuiceOrder("WJ","L")
    order2 = JuiceOrder("OJ","R")
    order3 = JuiceOrder("PJ","L")

    order1.check_menu()
    order1.compute_price()
    print(order1.display_detail())

    order2.check_menu()
    order2.compute_price()
    print(order2.display_detail())

    order3.check_menu()
    order3.compute_price()
    print(order3.display_detail())
        

        