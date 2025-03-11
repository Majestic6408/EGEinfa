def convert(num ,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(1, 1000000):
    R = convert(N, 2)
    summ = sum(map(int, R))
    ostat = summ % 2
    ostat = str(ostat)
    R = R + ostat
    summ1 = sum(map(int, R))
    ostat1 = summ1 % 2
    ostat1 = str(ostat1)
    R = R + ostat1
    R = int(R, 2)
    if R > 75:
        ans.append(R)


print(min(ans))