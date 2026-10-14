import cmath

FILE_PATH = "zad_32_wspolczynniki.txt"

with open(FILE_PATH) as f:
    a, b, c = (float(x) for x in f.read().split())

if a == 0:
    print("a = 0, this is not a quadratic equation")
else:
    d = cmath.sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)

    print(f"{a}x^2 + {b}x + {c} = 0")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
