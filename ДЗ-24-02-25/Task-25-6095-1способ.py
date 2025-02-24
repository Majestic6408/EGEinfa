from itertools import product

ans = []
for r1 in range(5):
    for z1 in product('0123456789', repeat=r1):
        z1 = ''.join(z1)
        for r2 in range(r1 - 1):
            for z2 in product('01234567890', repeat=r2):
                z2 = ''.join(z2)

                num = int(f'{z1}15{z2}7424')

                u1 = num % 111 == 0
                u2 = num % 113 == 0
                u3 = num % 127 == 0
                f1 = u1 + u2 + u3 == 1
                if num <= 10 ** 8 and f1:
                    if num % 111 == 0:
                        ans.append([num, num // 111])
                    if num % 113 == 0:
                        ans.append([num, num // 113])
                    if num % 127 == 0:
                        ans.append([num, num // 127])

ans = sorted(ans)
for i in ans:
    print(*i)
