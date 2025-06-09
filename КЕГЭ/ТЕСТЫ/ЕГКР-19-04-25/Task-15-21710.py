from itertools import combinations

def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = A1 <= x <= A2
    return (not A) <= (B == C)

ans = []
len = [i + eps for i in range(33, 113) for eps in [0, 0.1, 0.9]]

for A1, A2 in combinations(len, 2):
    if all(f(x) for x in len):
        ans.append([A2 - A1])

print(min(ans))