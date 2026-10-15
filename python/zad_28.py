def solve(a: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]

    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[pivot] = m[pivot], m[i]

        for r in range(i + 1, n):
            factor = m[r][i] / m[i][i]
            m[r] = [x - factor * y for x, y in zip(m[r], m[i])]

    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]

    return x


#  2x + y -  z  =  8
# -3x - y + 2z  = -11
# -2x + y + 2z  = -3
a = [[2., 1., -1.], [-3., -1., 2.], [-2., 1., 2.]]
b = [8., -11., -3.]

print(f"x = {solve(a, b)}")
