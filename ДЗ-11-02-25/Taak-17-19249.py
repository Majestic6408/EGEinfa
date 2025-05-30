with open('17_19249.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if len(str(i)) == 5 and str(i)[-2:] == '43')
ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 ** 2 + num2 ** 2 + num3 ** 2

    u1 = len(str(abs(num1))) == 5 and str(num1)[-2:] == '43'
    u2 = len(str(abs(num2))) == 5 and str(num2)[-2:] == '43'
    u3 = len(str(abs(num3))) == 5 and str(num3)[-2:] == '43'

    f1 = u1 + u2 + u3 >= 1
    f2 = summ <= maxx ** 2

    if f1 and f2:
        ans.append(summ)

print(len(ans), min(ans))
