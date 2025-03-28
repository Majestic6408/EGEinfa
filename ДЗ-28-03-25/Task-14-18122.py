def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 5556):
    num = 5 ** 150 + 5 ** 135 - x
    num = convert(num, 5)
    ans.append([num.count('4'), x])

ans = sorted(ans)
print(ans)