def factorial(n: int) -> int:
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


n = int(input("n: "))
print(f"{n}! = {factorial(n)}")
