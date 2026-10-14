def bubble_sort(nums: list[int]) -> list[int]:
    nums = nums[:]
    n = len(nums)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    return nums


with open("zad_38_input.txt") as f:
    nums = [int(x) for x in f.read().split()]

with open("zad_38_a_output.txt", "w") as f:
    f.write(" ".join(map(str, bubble_sort(nums))) + "\n")
