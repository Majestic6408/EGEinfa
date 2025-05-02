def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(1, 2006)[::-1]:
    num = 43 ** 56 + 113 ** 841 - x
    num1 = convert(num, 4)
    chet = [1 for i in num1 if int(i) % 2 == 0]
    necht = [1 for i in num1 if int(i) % 2 != 0]
    if sum(chet) % 2 == 0 and sum(necht) % 2 == 0 and num1.count('2') <= 712:
        print(x)