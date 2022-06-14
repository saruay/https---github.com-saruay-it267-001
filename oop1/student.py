class Student:
    def __init__(self,id:str,name:str,major:str):
        self.id = id
        self.name = name
        self.major = major

    def display_detail(self):
        print(f"--------------------------------")
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"major: {self.major}")

    def __del__(self):
        print(f'Object was destroyed')
  
if __name__ == "__main__":
    jessica = Student("111","jessica","IT")
    john = Student("112","john","MKT")
    jessica.display_detail()
    john.display_detail()

