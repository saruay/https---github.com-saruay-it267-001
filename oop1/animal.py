class Animal:
    #class varible
    animal = "CAT" 

    def new_animal(self,name:str,breed:str,colour:str,age:int):
        #instance varible
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age

    def print_detail(self):
        print(f"--------------------------------")
        print(f"Name: {self.name}")
        print(f"Animal: {self.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print(f"Age: {self.age}")

    def __del__(self):
        print(f'Object was destroyed')

#create object
if __name__ == "__main__":
    Animal.animal = "FISH"
    ula = Animal()
    ula.new_animal("Ula","Scottish","White","1")
    ula.animal = "DOG"
    ula.print_detail()

    drac = Animal()
    drac.new_animal("Drac","Scottish","White","1")
    drac.print_detail()
    drac.breed = "Catfish"
    drac.print_detail()

    #เรียกดูข้อมูลขแง object ผ่านทางชื่อ class
    Animal.print_detail(ula) #ula.print_detail() มีค่าเท่ากัน
    Animal.print_detail(drac) #drac.print_detail()

    #เรียกดู class varibleทั้งหมด
    print(f"{Animal.__dict__}")

    #เรียกดู instance varibleทั้งหมด
    print(f"{ula.__dict__}")

    peter = Animal()
    peter.new_animal("Peter","Parrot","green yellow red","2")
    #add new attibute to peter
    peter.legs = 2
    print(f"{peter.__dict__}")
