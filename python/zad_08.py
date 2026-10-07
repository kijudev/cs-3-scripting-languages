# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

items = [42, True, False]
items.append("meaning of everything")
items.append([True, False])
items.append(42.42)
items.append("Functional programming is better")

print(*items, sep = '\n')

