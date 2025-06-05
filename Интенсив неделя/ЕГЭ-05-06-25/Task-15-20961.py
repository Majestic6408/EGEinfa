from itertools import combinations

def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = A1 <= x <= A2
    return not(not(Q <= (((not A) and P) <= (not Q))))

ans = []
len = [i + eps for i in range(13, 170) for eps in [0, 0.1, 0.9]]
for A1, A2 in combinations(len, 2):
    if all(f(x) for x in len):
        ans.append([A2 - A1])

print(min(ans))