from oop2.oop2.modulepackage2.measure import Measure

if __name__=='__main__':
    '''m1 = Measure(56)
    m2 = Measure(78)
    print(m1.inch_cm())
    print(m2.cm_inch())
    m3 = Measure(56)
    m4 = Measure(78)
    print(m3.inch_cm())
    print(m4.inch_cm())
    m5 = Measure(14)
    m6 = Measure(250)
    print(m1.cm_inch())
    print(m2.cm_inch())'''

    '''inch_list = [52,18,20,40]
    for item in inch_list:
        m = Measure
        print(m.inch_cm())'''

    num = float(input("Enter number: "))
    ch = input("Choose I(inch->cm),C(cm->inch):").upper()
    if ch == 'I':
        m = Measure(num)
        print(m.inch_cm())
    elif ch == 'C':
        m = Measure(num)
        print(m.cm_inch())
    else:
        print("Wrong Character")