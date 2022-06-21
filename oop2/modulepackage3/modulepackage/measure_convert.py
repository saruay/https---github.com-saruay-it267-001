from math import degrees


def inch_cm(inch: float):
    return f'{inch * 2.54:,.2f}'

def cm_inch(cm: float):
    return f'{cm / 2.54:,.2f}'

if __name__=='__main__':
    print()
    print()