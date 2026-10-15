import math


def polygon_area(sides: int, length: float) -> float:
    return sides * length ** 2 / (4 * math.tan(math.pi / sides))


sides = int(input("number of sides: "))
length = float(input("side length: "))

if sides < 3:
    print("polygon needs at least 3 sides")
else:
    print(f"area = {polygon_area(sides, length):.2f}")
