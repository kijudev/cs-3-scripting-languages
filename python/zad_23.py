text = input("text: ")
cleaned = "".join(c.lower() for c in text if c.isalnum())

if cleaned == cleaned[::-1]:
    print(f'"{text}" is a palindrome')
else:
    print(f'"{text}" is not a palindrome')
