def f(x, y, s):
    if x + y <= 72:
        return s % 2 == 0
    if s == 0:
        return 0
    h = [f(x - 3, y, s - 1),
         f(x, y - 3, s - 1),
         f(x // 2 if x % 2 == 0 else x // 2 + 1, y, s - 1),
         f(x, y // 2 if y % 2 == 0 else y // 2 + 1, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

s1 = 50
print([s for s in range(23, 150) if f(s, s1, 2)])
print([s for s in range(23, 150) if not f(s, s1, 1) and f(s, s1, 3)])
print([s for s in range(23, 150) if not f(s, s1, 2) and f(s, s1, 4)])