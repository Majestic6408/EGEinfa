def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 1000):
    R = convert(N, 2)
    if N % 3 == 0:
        R = R + R[-3:]
    else:
        ostat = (N % 3) * 3
        ostat1 = convert(ostat, 2)
        R = R + str(ostat1)
    R = int(R, 2)
    if R < 170:
        ans.append(R)

print(max(ans))