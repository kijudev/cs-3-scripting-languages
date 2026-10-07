# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

with open("zad_30_input.txt") as f:
    text = f.read()

with open("zad_30_wersaliki.txt", "w") as f:
    f.write(text.upper())
