class Power:
    def pow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.pow(x, -n)

        result = 1

        for _ in range(n):
            result *= x

        return result


x = float(input("x: "))
n = int(input("n: "))

if x == 0 and n < 0:
    print("0 cannot be raised to a negative power")
else:
    print(f"{x}^{n} = {Power().pow(x, n)}")
