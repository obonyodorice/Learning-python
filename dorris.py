# def trapezium_area(a, b):
#     height = 10

#     area = 0.5 * height * a + 0.5 * height * b

#     return f'The area of trapezium is {area}'

# trapezium_area(4, 5)


# class Trapezia:

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def area(self, height):
        
#         area = 0.5 *  height * self.a + 0.5 * height * self.b

#         return area  

# first = Trapezia(4, 6)
# print(first.area(10))
class Family:
    def __init__(self,Name,age,con):
        self.Name= Name
        self.age= age
        self.con= con

    def remarks(self):
            return f'{self.Name},You are a grown up now'

Child=Family('Name','age','con')
Child.Name=input('Enter your name:')
Child.age=input('Enter your age')
Child.con=input('Is the child old,(y/n)')

# print (f'name is:{Child.Name}')
# print(f'age is:{Child.age}')
while True:
    if Child.con == 'n':
        break
    elif Child.con== 'y':
        # print (f'name is:{Child.Name}')
        # print(f'age is:{Child.age}')

        # print(Child.remarks())
        # break
        # break

family(remarks)