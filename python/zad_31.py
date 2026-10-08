base = int(input("base: "))
count = int(input("count: "))

with open("zad_31.txt", "w") as file:
    file.write("| licznik | suma |\n")
    file.write("|---------|------|\n")
    file.writelines(f"| {i:<7} | {(base * i):<4} |\n" for i in range(count))
