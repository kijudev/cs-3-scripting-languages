with open("zad_30_input.txt") as f:
    text = f.read()

with open("zad_30_wersaliki.txt", "w") as f:
    f.write(text.upper())
