def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res [::-1]
ans = []
for N in range(1, 10000):
    R = convert(N, 2)
    summ = sum(map(int, R))
    ostat = summ % 2
    R = R + str(ostat)
    summ1 = sum(map(int, R))
    ostat1 = summ1 % 2
    R = R + str(ostat1)
    R = int(R, 2)
    if R > 123:
        ans.append(R)

print(min(ans))