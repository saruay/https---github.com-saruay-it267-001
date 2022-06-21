class Customer:
    def __init__(self) -> None:
        self.name = ''
        self.address = ''
        self.phone = ''

    def new_customer(self):
        self.name = input('Enter customer name: ')
        self.address = input('Enter customer name: ')
        self.phone = input('Enter customer name: ')

    def cus_info(self):
        return f'name: {self.name}\naddress:{self.address}\nphone{self.phone}'
