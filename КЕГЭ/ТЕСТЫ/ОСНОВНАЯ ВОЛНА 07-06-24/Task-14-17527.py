def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
cnt = 0
for x in range(1, 2031):
    num = 3 ** 100 - x
    num1 = convert(num, 3)
    ans.append([num1.count('0'), x])

ans = sorted(ans)
print(ans)



