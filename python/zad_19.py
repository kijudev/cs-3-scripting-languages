# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

import random

low = int(input("lower bound: "))
high = int(input("upper bound: "))
filename = input("file with a list: ") or "zad_19_input.txt"

with open(filename) as f:
    items = [line.strip() for line in f if line.strip()]

num = random.randint(low, high)
item = random.choice(items)

with open("zad_19_output.txt", "w") as f:
    f.write(f"{num}\n{item}\n")

print(f"{num=}, {item=}")
