from itertools import product

ans = []
for r in range(7):
    for k in range(1, 10000):
        if k % 2 != 0:
            for z in product(str(k), repeat=r):
                z = ''.join(z)
                for v in '2468':

                    num = int(f'{v}136{z}')
                    if num <= 10 ** 10 and num % 53191 == 0:
                        ans.append([num, num // 53191])

ans = sorted(ans)
for i in ans:
    print(*i)