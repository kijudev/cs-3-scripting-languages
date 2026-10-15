import cmath

z = complex(input("complex number (e.g. 5j): "))

print(f"arc length = {cmath.phase(z):.2f}")
