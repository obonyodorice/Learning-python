# def trapezium_area(a, b):
#     height = 10

#     area = 0.5 * height * a + height * b

#     return f'The area of trapezium is {area}'



class Trapezia:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self, height):
        
        area = 0.5 *  height * self.a + 0.5 * height * self.b

        return area  

first = Trapezia(4, 6)
print(first.area(10))