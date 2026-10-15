def absolute(x: float) -> float:
    return x if x >= 0 else -x


x = float(input("number: "))

print(f"|{x}| = {absolute(x)}")
