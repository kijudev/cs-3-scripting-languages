items_a = [42, True, False]
items_a.append("meaning of everything")
items_a.append([True, False])
items_a.append(42.42)
items_a.append("Functional programming is better")

items_b = [420, True, False]
items_b.append("meaning of everything")
items_b.append([True, False])
items_b.append(420.420)
items_b.append("Object oriented programming is not better")

def compare_list_items(a: list, b: list) -> bool:
    return all([x == y for x, y in zip(a, b)])

have_same_items = compare_list_items(items_a, items_b)
print(f"{have_same_items=}")
