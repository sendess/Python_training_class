import operator
print(dir(operator))

class Person:
    '''
    This is how to write documentation to class
    '''
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f'{self.name} {self.age}')
    def speak(self, to_speak):
        print(f'{self.name} says {to_speak}')

    @staticmethod
    def change_name(changed_name):
        Person.name = changed_name

    def __add__(self, other):
        return self.age + other.age
    def __sub__(self, other):
        return self.age - other.age
#p1 = Person()
#print(type(p1))
#p1.describe()

#p1.name = 'John'
#p1.age = 18

#p1.describe()

p1 = Person('John', 18)
print(type(p1))
p1.describe()

p2 = Person('Testing' , 20)
p3 = Person('Testing2' , 20)

p1.describe()
p2.describe()


print(p1.name)
print(p1.age)


print(Person.__doc__)

p1.speak('Hi')
p1.speak('Bye')

print(p1+p2)
print(p2-p1)


#Person vanne class cha rey
#Person is parent class
#esbata derive garna paryo
#student,teacher,worker


class Student(Person):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level
    def describe(self):
        print(f'{self.name} is {self.age} years old and is in grade {self.level}')
        
s1 = Student('Ramu', 18, 12)
s1.speak('Hadibba')
s1.describe()

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.salary = salary
    def describe(self):
        return super().describe()
        print(f'{self.name} is {self.age} years olf and earns {self.salary}')
t1 = Teacher('Fathom', 30 , 20000)
t1.describe()