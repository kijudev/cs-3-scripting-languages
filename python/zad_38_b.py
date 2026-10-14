def insertion_sort(nums: list[int]) -> list[int]:
    nums = nums[:]

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


with open("zad_38_input.txt") as f:
    nums = [int(x) for x in f.read().split()]

with open("zad_38_b_output.txt", "w") as f:
    f.write(" ".join(map(str, insertion_sort(nums))) + "\n")
