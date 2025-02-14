def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    R = convert(N, 2)
    if N % 3 == 0:
        R = R + R[-3:]
    if N % 3 != 0:
        ostat = N % 3
        ostat = int(ostat) * 3
        ostat = convert(ostat, 2)
        R = R + ostat
    if int(R, 2) < 170:
        ans.append(int(R, 2))

print(max(ans))