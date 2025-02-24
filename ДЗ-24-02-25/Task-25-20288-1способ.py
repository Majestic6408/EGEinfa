from itertools import product

ans = []
for r in range(6):
    for z in product('02468', repeat=r):
        z = ''.join(z)
        for v1 in '13579':
            for v2 in '13579':

                num = int(f'{z}12{v1}4{v2}')

                if num <= 10 ** 10 and num % 9231 == 0:
                    ans.append([num, num // 9231])

ans = sorted(ans)
for i in ans:
    print(*i)