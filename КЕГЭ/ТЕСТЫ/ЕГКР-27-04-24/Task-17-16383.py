with open('17_16383.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(i)[-2:] == '21' and len(str(abs(i))) == 5)
maxx = maxx ** 2
ans = []
for num1, num2 in zip(data, data[1:]):
    summ = num1 ** 2 + num2 ** 2

    u1 = len(str(abs(num1))) == 5 and str(num1)[-2:] == '21'
    u2 = len(str(abs(num2))) == 5 and str(num2)[-2:] == '21'

    f1 = u1 + u2 == 1
    f2 = summ >= maxx

    if f1 and f2:
        ans.append(num1 + num2)

print(len(ans), max(ans))
