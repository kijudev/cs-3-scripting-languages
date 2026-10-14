import math
import random


def calc_pi(iter: int) -> float:
    num = 0

    for _ in range(iter):
        x = random.random()
        y = random.random()

        if math.hypot(x, y) <= 1:
            num += 1

    return (num / iter) * 4


pi = calc_pi(1000)
print(f"{pi=}")
