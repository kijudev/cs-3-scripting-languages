# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

num = input("number: ")

for _ in range(7):
    print(*[num] * 5, sep="\t")
