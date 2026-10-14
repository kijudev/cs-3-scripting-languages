def min_max_mean(nums: list[float]) -> float:
    return (min(nums) + max(nums)) / 2


nums = [4, -2, 17, 8, 3.5, 11]
print(f"{nums=}")
print(f"(min + max) / 2 = {min_max_mean(nums)}")
