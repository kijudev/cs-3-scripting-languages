# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

import statistics

with open("zad_16.txt") as f:
    nums = [int(x) for x in f.read().split()]

print(f"{nums=}")
print(f"sum: {sum(nums)}")
print(f"mean: {statistics.mean(nums)}")
print(f"median: {statistics.median(nums)}")
