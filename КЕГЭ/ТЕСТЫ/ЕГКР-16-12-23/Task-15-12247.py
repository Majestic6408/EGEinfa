def f(A):
    for x in range(1, 100):
        f = (x & A == 0) or (not(x & 37 == 0)) or (not(x & 12 == 0))
        if not f:
            return 0
    return 1

ans = []
for A in range(1, 100):
    if f(A):
        ans.append(A)

print(max(ans))