from unicodedata import name
from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    """def __init__(self,name,area,pop) -> None:
        self.name = name
        self.area = area
        self.population = pop"""
    def __init__(self) -> None:
        #super().__init__() #ถ้าใช้ super () ไม่ต้องใส่
        Geographic.__init__(self) #ถ้าใช้แบบนี้ต้องใส่ (self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = pop

    def getpopulationdensity(self):
        return self.population / self.area

    def showdetail(self):
        print(f'Country: {self.name}')
        #สถานที่ตั้ง latitude และ longtitude
        print(f'Location: {self.getcordinate()}')

        #แสดงขนาดพื้นที่, จำนวนประชากร
        print(f'Population: {self.population:,d}')
        print(f'Area: {self.area:,.2f}')
        print(f'Density: {self.getpopulationdensity():,.2f}')

        #Time Zone,Climate,Temperature,Weather
        print(f'Time Zone: {self.gettimeZone()}')
        print(f'Climate: {self.getclimate}')
        print(f'Temperature(C): {self.getcelcius()}')
        print(f'Temperature(F): {self.getfahrenheit()}')
        print(f'Weather: {self.getweather()}')

        print('**************************************')
