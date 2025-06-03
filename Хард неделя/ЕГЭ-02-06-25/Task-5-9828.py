def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 1000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        ostat = N % 3
        ostat1 = ostat * 4
        ostat2 = convert(ostat1, 3)
        R = R + str(ostat2)
    R = int(R, 3)
    if R < 199:
        ans.append(N)

print(max(ans))