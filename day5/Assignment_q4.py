class shape:
    def area(self):
        return 0
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
class triangle(shape):
    def __init__(self, s1, s2, s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def area(self):
        s= (self.s1+self.s2+self.s3)/2
        area= (s*(s-self.s1)*(s-self.s2)*(s-self.s3))**0.5
        return area
shapes = [
    circle(5),
    rectangle(4, 6),
    triangle(3, 7,5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")