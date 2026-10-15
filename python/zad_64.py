VOWELS = "aeiouyąęó"


def count_vowels(text: str) -> int:
    return sum(1 for char in text.lower() if char in VOWELS)


text = input("text: ")

print(f"vowels: {count_vowels(text)}")
