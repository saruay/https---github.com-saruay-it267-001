class Horse:
    def __init__(self,max_height:float=200,name:str='Khan Khan',color:str='Grey') -> None:
        self.max_height = max_height
        self.name = name
        self.color = color

    def run(self):
        print(f'{self.name} is running')

    def show_name(self):
        print(f'Name:{self.name}')

    def show_info(self):
        print(f'Name:{self.name}\nColor:{self.color}\n{self.max_height} cm')