# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)

n = int(input("n: "))
print(f"{n}! = {factorial(n)}")
