def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


with open("zad_38_input.txt") as f:
    nums = [int(x) for x in f.read().split()]

with open("zad_38_c_output.txt", "w") as f:
    f.write(" ".join(map(str, quick_sort(nums))) + "\n")
