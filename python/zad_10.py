# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

items = [420, True, False]
items.append("meaning of everything")
items.append(420.420)
items.append("Object oriented programming is not better")
items.append("meaning of everything")
items.append("meaning of everything")

item = "meaning of everything"
n = items.count(item)

if n > 0:
    print(f"value: \"{item}\" appears in the list {n} times")
else:
    print(f"value: \"{item}\" does not appear in the list")

