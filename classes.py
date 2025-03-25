# class Parent:
#     hair_colour = 'Black'

# class Child(Parent):
#     pass

# dorice = Child()
# mom_dorice = Parent()

# print(f'The hair colour of mom_dorice is:{mom_dorice.hair_colour} and that of dorice is:{dorice.hair_colour}')
class student:
    best_colour='Pink'
class teacher(student):
    pass
Dorice= teacher()
Child_Dorice=student()
print(f'{Dorice.best_colour} is my favourite colour and that of my child is also {Child_Dorice.best_colour}')