class Vehicle:
    name = None
    speed = None
    manufacturer = None

    def __init__(self, name, speed, manufacturer):
        self.name = name
        self.speed = speed
        self.manufacturer = manufacturer

    def get_speed(self):
        return self.speed

    def display(self):
        print(f'{self.name}, {self.speed}, {self.manufacturer}')


class Car(Vehicle):
    horsepower = None

    def __init__(self, name, speed, manufacturer, horsepower):
        super().__init__(name, speed, manufacturer)
        self.horsepower = horsepower

    def display(self):
        print(f'{self.name}, {self.speed}, {self.manufacturer}, {self.horsepower}')


class Plane(Vehicle):
    engine = None

    def __init__(self, name, speed, manufacturer, engine):
        super().__init__(name, speed, manufacturer)
        self.engine = engine

    def display(self):
        print(f'{self.name}, {self.speed}, {self.engine}')


car1 = Car('A8', 220, 'Audi', 340)
print('Speed of car is:', car1.get_speed())
car1.display()
plane1 = Plane('777', 400, 'Boeing', 'jet')
print('speed of plane is:', plane1.get_speed())
plane1.display()
