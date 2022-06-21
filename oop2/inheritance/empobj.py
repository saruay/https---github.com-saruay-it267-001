from empit import EmpIT
from empmkt import Empmkt

#create object employee IT
mike = EmpIT("001","Mike",6000)
mike.add_skill("Python,JavaSrcipt")
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#create object marketing
anna = Empmkt("002","Anna",35000)
anna.emp_detail()
anna.mkt_salary()

#พนักงานแผนการตลาดชื่อ Paul มีเงินเดือน 45000 ได้รับคอมมิชชั่น 35% โดยทำงานอยู่จังหวัดเชียงใหม่
paul = Empmkt("003","Paul",45000)
paul.add_commission(35)
paul.add_location("Chiang Mhai")
paul.emp_detail()
paul.mkt_salary()