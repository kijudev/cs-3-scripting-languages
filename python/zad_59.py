VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def from_roman(text: str) -> int:
    result = 0

    for i, char in enumerate(text):
        value = VALUES[char]

        # smaller value before a bigger one is subtracted (IV = 4)
        if i + 1 < len(text) and value < VALUES[text[i + 1]]:
            result -= value
        else:
            result += value

    return result


text = input("roman number: ").upper()

if not text or any(char not in VALUES for char in text):
    print(f"'{text}' is not a roman number")
else:
    print(f"{text} = {from_roman(text)}")
