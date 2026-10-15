import math


def sin_sum(a: float, b: float) -> tuple[float, float]:
    return math.sin(a) + math.sin(b), 2 * math.sin((a + b) / 2) * math.cos((a - b) / 2)

def sin_diff(a: float, b: float) -> tuple[float, float]:
    return math.sin(a) - math.sin(b), 2 * math.sin((a - b) / 2) * math.cos((a + b) / 2)

def binomial(x: float, n: int) -> tuple[float, float]:
    return (1 + x) ** n, sum(math.comb(n, k) * x ** k for k in range(n + 1))

def quadratic(a: float, b: float, c: float) -> tuple[complex, complex]:
    d = math.sqrt(b ** 2 - 4 * a * c)
    return (-b + d) / (2 * a), (-b - d) / (2 * a)

def exp(x: float, terms: int = 30) -> tuple[float, float]:
    return math.exp(x), sum(x ** n / math.factorial(n) for n in range(terms))

def fourier(x: float, L: float, terms: int = 1000) -> tuple[float, float]:
    a0 = 0
    total = a0

    for n in range(1, terms + 1):
        an = 0
        bn = 2 * L * (-1) ** (n + 1) / (n * math.pi)
        total += an * math.cos(n * math.pi * x / L) + bn * math.sin(n * math.pi * x / L)

    return x, total

print(f"(a) sin+: {sin_sum(1.2, 0.5)}")
print(f"(a) sin-: {sin_diff(1.2, 0.5)}")
print(f"(b) {binomial(0.3, 5)}")
print(f"(c) {quadratic(1, -3, 2)}")
print(f"(d) {exp(2)}")
print(f"(e) {fourier(1, math.pi)}")
