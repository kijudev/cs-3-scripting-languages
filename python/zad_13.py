# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

text = input("text: ").lower()

for vowel in "aeiouyąęó":
    n = text.count(vowel)

    if n > 0:
        print(f"{vowel}: {n}")
