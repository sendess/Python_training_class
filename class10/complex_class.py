class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def abs_value(self):
        return(self.real ** 2 + self.imag ** 2)**0.5
    
    def __add__ (self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__ (self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __str__ (self):
        return '{} + {}i'.format(self.real, self.imag)
c1 = Complex(1, 2)
c2 = Complex(3,4)
print(c1)
print(c1+c2)
print(c2-c1)


class Parent:
    def __init__(self, x, y, z):
        self.__x = x  # Private
        self._y = y   # Protected
        self.z = z    # Public
    
    def view(self): 
        print(f'{self.x} {self.y} {self.y}')
class Child(Parent):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

c = Child(4, 5, 6)
p = Parent(1, 2, 3)

#print(p.view())

print(dir(p))
print(dir(c))

print(p._Parent__x)
print(p._y)