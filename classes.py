class Parent:
    hair_colour = 'Black'

class Child(Parent):
    pass

dorice = Child()
mom_dorice = Parent()

print(f'The hair colour of mom_dorice is:{mom_dorice.hair_colour} and that of dorice is:{dorice.hair_colour}')