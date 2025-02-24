from itertools import product

ans = []
for r in range(4):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':
            num = int(f'1{v}2139{z}4')

            if num <= 10 ** 10 and num % 3052 == 0:
                ans.append([num, num // 3052])

ans = sorted(ans)
for i in ans:
    print(*i)