num = input("number: ")

with open("zad_21.txt", "w") as f:
    for _ in range(7):
        print(*[num] * 5, sep='\t', file=f)
