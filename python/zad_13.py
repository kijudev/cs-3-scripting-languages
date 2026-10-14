text = input("text: ").lower()

for vowel in "aeiouyąęó":
    n = text.count(vowel)

    if n > 0:
        print(f"{vowel}: {n}")
