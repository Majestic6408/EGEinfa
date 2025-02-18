from itertools import product

ans = []
for r in range(3):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':
            num = int(f'12{z}4{v}65')

            if num <= 10 ** 8 and num % 161 == 0:
                ans.append([num, num // 161])

ans = sorted(ans)
for i in ans:
    print(*i)