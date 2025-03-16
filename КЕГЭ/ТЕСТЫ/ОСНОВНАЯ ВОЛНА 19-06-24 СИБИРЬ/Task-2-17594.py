from itertools import permutations, product

def f(x, y, z, w):
    return ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [
        (1, a1, a2, a3),
        (0, a4, 1, a5),
        (a6, 0, 0, a7)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)