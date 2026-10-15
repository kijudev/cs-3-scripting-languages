with open("zad_25_input.txt") as f:
    num = int(f.read())

with open("zad_25_output.txt", "w") as f:
    print(num, hex(num), oct(num), sep="\n", file=f)
