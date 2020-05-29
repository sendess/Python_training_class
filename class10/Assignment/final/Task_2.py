#       Task 2
#       Create a class name 'Vehicle' with attributes 'name', 'speed' and 'manufacturer' 
#       and a method to get the speed. Further extend this class into two other classes 
#       named 'Car' and 'Plane' with car having attributes 'horsepower' for 'Car' and 
#       'engines' for 'Plane'. Use constructors to initialize the initial values

#       defining class
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

    def get_name(self):
        return self.name

    def get_manufacturer(self):
        return self.manufacturer
            
    def display(self):
        print(f'Name: {self.name},\n Top speed: {self.speed},\n Manufactured by: {self.manufacturer}')

#       derived class
class Car(Vehicle):
    horsepower = None

    def __init__(self, name, speed, manufacturer, horsepower):
        super().__init__(name, speed, manufacturer)
        self.horsepower = horsepower

    def display(self):
        print(f'Name: {self.name},\n Top speed: {self.speed} kmph ,\n Manufactured by: {self.manufacturer},\n Horsepower: {self.horsepower} hp.')

#       derived class
class Plane(Vehicle):
    engine = None

    def __init__(self, name, speed, manufacturer, engine):
        super().__init__(name, speed, manufacturer)
        self.engine = engine

    def display(self):
        print(f'Name: {self.name},\n Top speed: {self.speed} kmph,\n Manufactured by: {self.manufacturer},\n Engine: {self.engine}.')

#       creatng objects
object_car_1 = Car('Aventador', 352, 'Lamborghini', 730)
object_plane_1 = Plane('Wide-body jet airliner', 914, 'Airbus', 'Rolls-Royce Trent 500')

print('\n\n')
print('Detail of car_1 :')
object_car_1.display()
print('\n\n')
print('Details of plane_1 :')
object_plane_1.display()
