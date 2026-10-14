def factorial(n: int) -> int:
    if n <= 1:
        return 1

    return n * factorial(n - 1)


n = int(input("n: "))
print(f"{n}! = {factorial(n)}")
