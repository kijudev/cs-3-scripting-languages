import statistics

with open("zad_16.txt") as f:
    nums = [int(x) for x in f.read().split()]

print(f"{nums=}")
print(f"sum: {sum(nums)}")
print(f"mean: {statistics.mean(nums)}")
print(f"median: {statistics.median(nums)}")
