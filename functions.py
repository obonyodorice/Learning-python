#     print(f'Good {time} {name} Hope you are fine')
# greet('Dorice','Morning')

class Students:
    def __init__(Self,Name,Stream,Adm,Grade,Func):
        Self.Name=Name
        Self.Stream=Stream
        Self.Adm=Adm
        Self.Grade=Grade
        Self.Func=Func

    def remarks(Self):
       return f'{Self.Name} is proceeding to the next class'

Pass= Students('Name','Stream','Adm','Grade','Func')
Pass.Name=input('Enter the name:')
Pass.Stream=input('Enter the Stream:')
Pass.Adm=input('Enter the Adm:')
Pass.Grade=input('Grade is:')
Pass.Func=input('Did he/she pass:(y/n)')

if Pass.Func=='n':
   break
elif Pass.Func=='y':

 print(f'Name is:{Pass.Name}') 
 print(f'Stream:{Pass.Stream}')   
 print(f'Admission no.:{Pass.Adm}')
 print(f'Overral Grade:{Pass.Grade}')
 
 print(Pass.remarks())