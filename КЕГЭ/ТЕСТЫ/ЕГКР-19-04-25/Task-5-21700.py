def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(3, 10000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        ostat = (N % 3) * 3
        ostat1 = convert(ostat, 3)
        R = R + str(ostat1)
    R = int(R, 3)
    if R < 150:
        ans.append(N)

print(max(ans))