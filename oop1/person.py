class Person:
    def __init__(self,name,gender,profession,hours) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.hours = hours
        
    def work(self):
        print(f"{self.name} is working as a {self.profession}")

    def study(self):
        print(f"{self.name} studies for {self.hours} hours(s)")

    def show(self):
        print(f"Name:{self.name} Gender:{self.gender} Profession:{self.profession} Study:{self.hours}")

#create object
jessa = Person("jessa","Female","Software Engineer","10")
jessa.show()
jessa.work()
jessa.study()

jon = Person("jon","Male","Doctor","15")
jon.show()
jon.work()
jon.study()

lalisa = Person("lalisa","Female","Korean Singer","13")
lalisa.work()