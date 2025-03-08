def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 2)
    if N % 3 == 0:
        R = R + R[-2:]
    if N % 3 != 0:
        ostat = N % 3
        ostat = ostat * 3
        ostat = convert(ostat, 2)
        R = R + ostat
    R = int(R, 2)
    if R >= 195:
        ans.append(R)

print(min(ans))
