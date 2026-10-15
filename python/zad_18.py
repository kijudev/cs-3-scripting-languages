def get_number(prompt: str) -> int | float | complex:
    text = input(prompt)

    for kind in (int, float, complex):
        try:
            return kind(text)
        except ValueError:
            pass

    print("that is not a number, try again")
    return get_number(prompt)


num = get_number("number: ")
print(f"{num=}, type: {type(num).__name__}")
