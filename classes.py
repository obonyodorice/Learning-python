# class Parent:
#     hair_colour = 'Black'

# class Child(Parent):
#     pass

# dorice = Child()
# mom_dorice = Parent()

# print(f'The hair colour of mom_dorice is:{mom_dorice.hair_colour} and that of dorice is:{dorice.hair_colour}')
# class student:
#     best_colour='Pink'
# class teacher(student):
#     pass
# Dorice= teacher()
# Child_Dorice=student()
# print(f'{Dorice.best_colour} is my favourite colour and that of my child is also {Child_Dorice.best_colour}')
class Car:
    def __init__(self,Brand, Horsepower):
        self.Brand=Brand
        self.Horsepower=Horsepower
    def __str__(self):
        return f'{self.Brand} with {self.Horsepower}hp'

    # def __add__(self,other):
    #     return f'{self.Brand} & {other.Brand}'
    def Drive(self):
        return f'{self.Brand} is driving'
    # def speed(self):
    #     print(f'{self.Brand} with {self.Horsepower} Horsepower')
Toyota=Car('Toyota',200)
# Volvo=Car('Volvo',240)
print(Toyota)
# print(Toyota + Volvo)
Toyota.Drive()
# Toyota.speed()
    
