from condo import Condo

ideo = Condo("ideo5",18,"Lardphrao",80,"Condo 20 Floors")
ideo.show()

from project import Project
home = Project("Ladawan",15,"Bang Yai")
home.show()
home.update_budget(30)
print(f'budget: {home.get_budget()} MB')