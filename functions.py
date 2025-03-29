#     print(f'Good {time} {name} Hope you are fine')
# greet('Dorice','Morning')


# class Students:  #class in python
    
#     def __init__(Self,Name,Stream,Adm,Grade,Func):
#         Self.Name=Name
#         Self.Stream=Stream
#         Self.Adm=Adm
#         Self.Grade=Grade
#         Self.Func=Func

#     def remarks(Self):
#        return f'{Self.Name} is proceeding to the next class'

# Pass= Students('Name','Stream','Adm','Grade','Func')  #an instance of a class
# Pass.Name=input('Enter the name:')
# Pass.Stream=input('Enter the Stream:')
# Pass.Adm=input('Enter the Adm:')
# Pass.Grade=input('Grade is:')
# Pass.Func=input('Did he/she pass:(y/n)')


# while True:

#     my_dict = {
#         'name': Pass.Name,
#         'stream': Pass.Stream,
#         'adm': Pass.Adm,
#         'grade': Pass.Grade,

#     }

#     if Pass.Func == 'n':
#         break

#     if Pass.Func == 'y':

#         print(f'Name is:{Pass.Name}') 
#         print(f'Stream:{Pass.Stream}')   
#         print(f'Admission no.:{Pass.Adm}')
#         print(f'Overral Grade:{Pass.Grade}')
#         print(Pass.remarks())
#         break

# Fail=Students('Name','Stream','Adm','Grade','Func')
# Fail.Name=input('Enter the name:')
# Fail.Stream=input('Enter the Stream:')
# Fail.Adm=input('Enter the Adm:')
# Fail.Grade=input('Grade is:')
# Fail.Func=input('Did he/she pass:(y/n)')
# while True:
#     if Fail.Func == 'y':
#         break

#     if Fail.Func == 'n':

 
#         print(f'Name is:{Fail.Name}') 
#         print(f'Stream:{Fail.Stream}')   
#         print(f'Admission no.:{Fail.Adm}')
#         print(f'Overral Grade:{Fail.Grade}')

#         # print(Pass.remarks()) 
#         break
# print(Pass.remarks())     
from datetime import datetime
print('This is the current date')
print(datetime.now())