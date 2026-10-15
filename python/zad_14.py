while True:
    try:
        num = float(input("number: "))
        break
    except ValueError:
        print("that is not a valid number, try again")

print(f"{num=}")
