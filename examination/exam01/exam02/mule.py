from horse import Horse
from donkey import Donkey
class Mule(Horse,Donkey):
    def __init__(self,name,color,max_height,age,weight) -> None:
        self.name = name
        self.color = color
        self.max_height = max_height
        self.age = age
        self.weight = weight

    def run(self):
        print('Mule is running')

    def show_info(self):
        print(f'Name:{self.name}\nColor:{self.color}\nAge:{self.age}\nWeight:{self.weight}')

mule1 = Mule('Mumu')
mule1.color('Blue-eyed cream') 
mule1.age(3)
mule1.weight(200)
mule1.show_info()
print()

mule2 = Mule('Meme')
mule2.color('Palomino') 
mule2.age(1)
mule2.weight(120.7)
mule2.show_info()
print()