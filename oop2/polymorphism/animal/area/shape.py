class Shape:
    def __init__(self,shape) -> None:
        self.__shape = shape
        self.__area = 0

    @property
    def shape(self):
        return self.__shape
    @shape.setter
    def shape(self,value):
        self.__shape = value

    @property 
    def area(self):
        return self.__area
    @area.setter
    def area(self,value):
        self.__area = value

    
    def computer_area(self):
        pass

        