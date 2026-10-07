# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("that is not an integer, try again")


num = get_int("integer: ")
print(f"{num=}")
