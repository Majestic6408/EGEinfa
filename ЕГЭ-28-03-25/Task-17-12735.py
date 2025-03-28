with open('17_12735.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(i)[-2:] == '09')
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    summ = num1 + num2 + num3
    summ1 = num1 * num2 * num3

    u1 = num1 % 7 == 0
    u2 = num2 % 7 == 0
    u3 = num3 % 7 == 0
    f1 = u1 + u2 + u3 == 2
    f2 = summ < maxx
    if f1 and f2:
        ans.append(summ1)

print(len(ans), min(ans))