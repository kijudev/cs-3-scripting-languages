import itertools

genders = ["Kobieta", "Mężczyzna"]
colors = ["biały", "czarny", "zielony", "czerwony", "niebieski", "żółty", "szary"]
sizes = ["XXL", "XL", "L", "M", "S", "XS"]

combinations = itertools.product(genders, colors, sizes)

for i, (gender, color, size) in enumerate(combinations, start=1):
    with open(f"zad_34_metka_{i}.txt", "w") as f:
        f.write(f"płeć: {gender}\nkolor: {color}\nrozmiar: {size}\n")

print(f"created {i} labels")
