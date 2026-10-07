# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

while True:
    try:
        num = float(input("number: "))
        break
    except ValueError:
        print("that is not a valid number, try again")

print(f"{num=}")
