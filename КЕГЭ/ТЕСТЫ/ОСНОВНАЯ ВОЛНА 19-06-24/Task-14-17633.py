def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 2031):
    num = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    num = convert(num, 6)
    ans.append([num.count('0'), x])

ans = sorted(ans)

print(ans)

