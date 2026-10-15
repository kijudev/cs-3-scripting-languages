import random

cols = int(input("columns: "))
rows = int(input("rows: "))
low = int(input("lower bound: "))
high = int(input("upper bound: "))

with open("zad_22.txt", "w") as f:
    for _ in range(rows):
        print(*[random.randint(low, high) for _ in range(cols)], sep="\t", file=f)
