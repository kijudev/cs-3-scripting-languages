import statistics

nums = [int(x) for x in input("integers separated by spaces: ").split()]

print(f"sum: {sum(nums)}")
print(f"mean: {statistics.mean(nums)}")
print(f"median: {statistics.median(nums)}")
