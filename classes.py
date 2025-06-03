class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, studying {self.course}.")

    def is_adult(self):
        return self.age >= 18


name = input("What's your name? ")
age = int(input("..and your age? ")) 
course = input("What course do you pursue? ")

# Create a Student instance
student1 = Student(name, age, course)


print(f'\nName is: {student1.name}')
print(f'Age is: {student1.age}')
print(f'Course is: {student1.course}\n')


student1.introduce()

if student1.is_adult():
    print("This student is an adult.")
else:
    print("This student is not an adult.")
