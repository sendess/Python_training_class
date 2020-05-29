PI = 3.1415


class Circle:
    radius = None

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return PI * self.radius ** 2

    def ger_perimeter(self):
        return 2 * PI * self.radius

obj = Circle(7)
obj1 = Circle(4)

print(obj.ger_perimeter())
print(obj.get_area())

print(obj1.ger_perimeter())
print(obj1.get_area())