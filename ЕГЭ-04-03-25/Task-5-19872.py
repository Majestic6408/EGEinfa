def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 1000):
    R = convert(N, 7)
    if N % 2 == 0:
        R = '52' + R + '1'
    else:
        chisl_1 = R[0]
        chisl_2 = R[-1]
        R = chisl_2 + R[1:-1] + chisl_1 + '15'
    while R[0] == '0':
        R = R[1:]
    R = int(R)
    cnt = 0
    while R:
        cnt += 1
        R //= 10
    if cnt == 4:
        ans.append(N)

print(max(ans))