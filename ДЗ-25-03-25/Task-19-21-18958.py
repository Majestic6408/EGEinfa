def f(x, s):
    if x > 665:
        return s % 2 == 0
    if s == 0:
        return 0
    h = [f(x + 3, s - 1), f(x * 3, s - 1), f(x + x ** 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print([s for s in range(1, 666) if f(s, 2)])
print([s for s in range(1, 666) if not f(s, 1) and f(s, 3)])
print([s for s in range(1, 666) if f(s, 4) and not f(s, 2)])