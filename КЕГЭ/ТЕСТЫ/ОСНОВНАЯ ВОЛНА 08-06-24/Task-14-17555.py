def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 2031):
    num = 7 ** 91 + 7 ** 160 - x
    num1 = convert(num, 7)
    ans.append([num1.count('0'), x])

ans = sorted(ans)

print(ans)