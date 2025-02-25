# def greet(name,time):
#     print(f'Good {time} {name} Hope you are fine')
# greet('Dorice','Morning')
class Planet:
    def __init__(self):
        self.name='Earth'
        self.radius=3600
        self.gravity=9.8
        self.system='Earth system'
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

Earth= Planet()
print(f'Name is:{Earth.name}')  
print(f'radius is:{Earth.radius}') 
print(f'gravity is:{Earth.gravity}') 
print(f'system is:{Earth.system}') 
print(Earth.orbit())
