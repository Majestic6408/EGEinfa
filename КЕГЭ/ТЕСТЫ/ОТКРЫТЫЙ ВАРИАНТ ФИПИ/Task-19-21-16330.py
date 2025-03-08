def f(x, y, s):
    if x + y >= 59:
        return s % 2 == 0
    if s == 0:
        return 0
    h = [f(x + 1, y, s - 1), f(x, y + 1, s - 1), f(x * 2, y, s - 1), f(x, y * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

s1 = 5
print([s for s in range(1, 54) if f(s1, s, 2)])
print([s for s in range(1, 54) if not f(s1, s, 1) and f(s1, s, 3)])
print([s for s in range(1, 54) if not f(s1, s, 2) and f(s1, s, 4)])