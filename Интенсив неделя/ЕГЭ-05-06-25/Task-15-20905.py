from itertools import combinations

def f(x):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

ans = []
len = [x/10 for x in range(15 * 10, 82 * 10)]
for A1, A2 in combinations(len, 2):
    if all(f(x) for x in len):
        ans.append([A2 - A1])

print(min(ans))