class WordReverser:
    def __init__(self, text: str):
        self.text = text

    def reverse(self) -> str:
        return " ".join(reversed(self.text.split()))


text = input("text: ") or "Jestem studentem. Jestem studentem."

print(WordReverser(text).reverse())
