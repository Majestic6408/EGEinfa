with open('17_9748.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(i)[-2:] == '15')
ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i], data[i + 1], data[i + 2]
    summ = num1 + num2 + num3

    u1 = len(str(num1)) == 4
    u2 = len(str(num2)) == 4
    u3 = len(str(num3)) == 4

    f1 = u1 + u2 + u3 == 1
    f2 = summ >= maxx

    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))

