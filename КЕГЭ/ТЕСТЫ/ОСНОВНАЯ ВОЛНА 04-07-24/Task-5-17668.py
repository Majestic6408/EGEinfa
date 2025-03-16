def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(28, 100000):
    R = convert(N, 2)
    summ = sum(map(int, R))
    if summ % 2 == 0:
        R = '10' + R[2:] + '0'
    if summ % 2 != 0:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    ans.append(R)

print(min(ans))