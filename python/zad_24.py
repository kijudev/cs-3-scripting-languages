def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)

n = int(input("n: "))
print(f"{n}! = {factorial(n)}")
