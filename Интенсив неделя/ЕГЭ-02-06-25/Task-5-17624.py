def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 230):
    R = convert(N, 2)
    ostat = N % 2
    R = R + str(ostat)
    ostat1 = sum(map(int, R)) % 2
    R = R + str(ostat1)
    R = int(R, 2)
    if R > 75:
        ans.append(R)

print(min(ans))