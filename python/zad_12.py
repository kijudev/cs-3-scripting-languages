# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

print(
    'The program is going to ask for a list of number; if you wish to end your input please write "end"'
)

items: list[str] = []

while True:
    item = input(f"{len(items) + 1}. ")

    if item.lower().strip() == "end":
        break

    items.append(item)

print("----")
print(*items, sep = '\n')

