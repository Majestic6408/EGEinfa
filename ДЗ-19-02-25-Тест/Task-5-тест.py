def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 4)
    if len(R) % 2 == 0:
        if len(R) == 2:
            R = R[:1] + '0' + R[1:]
        if len(R) == 4:
            R = R[:2] + '0' + R[2:]
        if len(R) == 6:
            R = R[:3] + '0' + R[3:]
        if len(R) == 8:
            R = R[:4] + '0' + R[4:]
    R = int(R, 10)
    if R <= 180:
        ans.append(N)

print(ans)