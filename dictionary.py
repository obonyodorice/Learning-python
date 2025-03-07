sibling=()
def Sibling_intro(Dictionary):

    for key,val in Dictionary.items():
        print(f'I am {key} and {val} is my favourite colour')
        Sibling_colours={}
    while True:
        Sibling_name =input('My name is:')
        Sibling_colour=input('My favourite colour is is:')
        Sibling_colours[Sibling_name]=Sibling_colour   

        another=input('add another(y/n)')
        if another=='n':   
            break

Sibling_intro(Dictionary)
   





# family = {
#     'Dorice': 'Blue',
#     'Reagan': 'Pink',
#     'Becky': 'Green',
#     'Ashley': 'Purple'
# }

# def Sibling_intro(Dictionary):
#     for key,val in Dictionary.items():
#         print(f'I am {key} and {val} is my favourite colour')

# Sibling_intro(family)