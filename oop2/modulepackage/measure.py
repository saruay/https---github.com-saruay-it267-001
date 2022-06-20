from ast import Num


class Measure:
    def __init__(self,num:float) -> None:
        self.num = num
    
    def inch_cm(self):
        return f'{self.num * 2.54:,.2f}'

    def cm_inch(self):
        return f'{self.num / 2.54:,.2f}'

if __name__=='__main__':
    m1 = Measure(12.5)
    m2 = Measure(100)
    print(m1.inch_cm())
    print(m2.cm_inch())
    m3 = Measure(56)
    m4 = Measure(78)
    print(m3.inch_cm())
    print(m4.inch_cm())
    m5 = Measure(14)
    m6 = Measure(250)
    print(m1.cm_inch())
    print(m2.cm_inch())