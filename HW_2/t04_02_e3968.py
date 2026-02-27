def solve(C):
    l = 0.0
    r = 100000.0

    for i in range(100):
        m = l + (r - l) / 2.0

        if m * m + m ** 0.5 < C:
            l = m
        else:
            r = m
    return l

C = float(input())
ans = solve(C)
print(f"{ans:.9f}")