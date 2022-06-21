class Employee:
    def __init__(self,id,name,salary) -> None:
        self.id = id
        self.name = name
        self._salary = salary #มี # ข้างหน้าจะมี _

    def emp_detail(self):
        print(f'id: {self.id}')
        print(f'name: {self.name}')

    def _emp_salary(self): #มี _ เพราะมี # ข้างหน้า
        print(f'salary:{self._salary}')