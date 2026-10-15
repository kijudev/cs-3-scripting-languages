import random

FILE_PATH = "zad_57_input.txt"


def random_item(filename: str) -> str:
    with open(filename) as f:
        items = [line.strip() for line in f if line.strip()]

    return random.choice(items)


print(random_item(FILE_PATH))
