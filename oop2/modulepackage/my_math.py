PI = 3.416

def square(number):
    #
    return (number ** 2)

def circle_area(radius):
    area = PI * radius * radius
    return area

if __name__=="__main__":
    print(square(5))
    print(circle_area(1))
    print(PI)