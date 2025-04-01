def f(x, y, s):
    if x + y >= 44:
        return s % 2 == 0
    if s == 0:
        return 0
    h = [f(x + y, y, s - 1), f(x, y + x, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

s1 = 11
print([s for s in range(1, 10000) if f(s1, s, 1)])
print([s for s in range(1, 10000) if f(s1, s, 2)])

ans = []
for s1 in range(0, 30):
    for s2 in range(0, 30):
        if f(s1, s2, 3):
            ans.append([abs(s1 - s2), s1, s2])

print(min(ans))