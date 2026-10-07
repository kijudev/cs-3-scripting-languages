# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

letters = input("letters to count: ").lower()

with open("zad_27.txt") as f:
    text = f.read().lower()

for letter in letters:
    print(f"{letter}: {text.count(letter)}")
