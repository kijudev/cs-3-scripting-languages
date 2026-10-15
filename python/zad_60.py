import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

    def perimeter(self) -> float:
        return self.circumference()


r = float(input("radius: "))
c = Circle(r)

print(f"area = {c.area():.2f}")
print(f"circumference = {c.circumference():.2f}")
print(f"perimeter = {c.perimeter():.2f}")
