class Donkey:
    def __init__(self,age:int=2,weight:float=100) -> None:
        self.age = age
        self.weight = weight

    def sound(self):
        print(f'Donkey make eeyore sound')

    def show_info(self):
        print(f'Age:{self.age}-year-old\nWeight:{self.weight}')