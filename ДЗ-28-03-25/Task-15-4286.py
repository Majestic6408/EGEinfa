from itertools import combinations

def f(x):
    P = 1 <= x <= 98
    Q = 25 <= x <= 42
    A = A1 <= x <= A2
    return Q <= ((not P and Q) <= A)

ans = []
line = [x / 10 for x in range(1 * 10, 44 * 10)]
for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))