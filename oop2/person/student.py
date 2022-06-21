from person import Person

class Student(Person):
    def __init__(self,name,faculy,major,year) -> None:
        super().__init__(name)
        self.faculry= faculy
        self.major = major
        self.year = year

    def welcome(self):
        super().welcome()
        print(f'welcome to {self.faculry} major {self.major} in {self.year}')