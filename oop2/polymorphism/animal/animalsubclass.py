from animal import Animal

class Dog(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    def info(self):
        #super().info() เปลี่ยนไปใช้ Animal ได้
        Animal.info(self) # จะได้ข้อความม animal info มา
        print('I am a dog')
        print(f'My name is {self.name}.')
        print(f'I am {self.age} year old. ')
    
    def make_sound(self):
        #super().make_sound() เปลี่ยนไปใช้ Animal
        Animal.make_sound(self) #จะได้ข้อความ animal make sound มา
        print(f'Hey! I make Woof!! Woof!! sound. ')

class Cat(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    def info(self):
        #super().info() เปลี่ยนไปใช้ Animal ได้
        Animal.info(self) # จะได้ข้อความม animal info มา
        print('I am a cat')
        print(f'My name is {self.name}.')
        print(f'I am {self.age} year old. ')
    
    def make_sound(self):
        #super().make_sound() เปลี่ยนไปใช้ Animal
        Animal.make_sound(self) #จะได้ข้อความ animal make sound มา
        print(f'Hey! I make Meow!! Meow!! sound. ')

class Cow(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    def info(self):
        #super().info() เปลี่ยนไปใช้ Animal ได้
        Animal.info(self) # จะได้ข้อความม animal info มา
        print('I am a cow')
        print(f'My name is {self.name}.')
        print(f'I am {self.age} year old. ')
    
    def make_sound(self):
        #super().make_sound() เปลี่ยนไปใช้ Animal
        Animal.make_sound(self) #จะได้ข้อความ animal make sound มา
        print(f'Hey! I make Moo!! Moo!! sound. ')