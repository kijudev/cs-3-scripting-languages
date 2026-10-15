a = complex(input("first complex number (e.g. 1+2j): "))
b = complex(input("second complex number (e.g. 3-4j): "))

if b == 0:
    print("cannot divide by zero")
else:
    print(f"{a} / {b} = {a / b}")
