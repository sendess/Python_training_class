#       Task 1
#       Create a class named 'Circle' with an attribute 'radius' and two
#       methods that returns area and perimeter of the circle respectively.

#       defining class
class Circle:
    radius = None

    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return ((22 / 7) * self.radius * self.radius)

    def calc_circumference(self):
        return (2 * (22 / 7) * self.radius)


circle_1 = int(input("Enter the radius of your object circle : "))
#       creating object
circle_object_1 = Circle(circle_1)
print("The circumference of circle 1 is : ",circle_object_1.calc_circumference())
print("The area of circle 1 is : ", circle_object_1.calc_area())
