from collections import Counter

with open("zad_29.txt") as f:
    words = [w.strip(".,;:!?\"'()-").lower() for w in f.read().split()]
    words = [w for w in words if w]

print(f"number of words:     {len(words)}")
print(f"unique words:        {len(set(words))}")
print(f"average word length: {sum(map(len, words)) / len(words):.2f}")
print(f"longest word:        {max(words, key=len)}")
print("----")

for word, n in Counter(words).most_common():
    print(f"{word}: {n}")
