# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

import statistics

nums = [int(x) for x in input("integers separated by spaces: ").split()]

print(f"sum: {sum(nums)}")
print(f"mean: {statistics.mean(nums)}")
print(f"median: {statistics.median(nums)}")
