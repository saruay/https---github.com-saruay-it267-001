from employee import Employee

class Empmkt(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location = 'Bangkok'
        self.commission = 30
        self.department = 'Marketing'

    def add_location(self,location):
        self.location = location

    def add_commission(self,commission):
        self.commission = commission

    def emp_detail(self):
        print('------ Employee Marketing Detail ------')
        super().emp_detail()
         #เรียกใช้ method emp_detail ของคลาส Employee เพื่อแสดง id,name
        print(f'location: {self.location}')
        print(f'commission: {self.commission} %')
    
    def mkt_salary(self):
        self._emp_salary()
