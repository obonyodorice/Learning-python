#     print(f'Good {time} {name} Hope you are fine')
# greet('Dorice','Morning')

class Students:
    def __init__(Self,Name,Stream,Adm,Position):
        Self.Name=Name
        Self.Stream=Stream
        Self.Adm=Adm
        Self.Position=Position

    def remarks(Self):
       return f'{Self.Name}is proceeding to the next class'

Pass= Students('Dorice','Mars 3','13699','1')
print(f'Name is:{Pass.Name}') 
print(f'Stream:{Pass.Stream}')   
print(f'Admission no.:{Pass.Adm}')
print(f'Overral position:{Pass.Position}')
print(Pass.remarks())