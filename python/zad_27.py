letters = input("letters to count: ").lower()

with open("zad_27.txt") as f:
    text = f.read().lower()

for letter in letters:
    print(f"{letter}: {text.count(letter)}")
