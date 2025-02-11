with open('17_9786.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(i)[-2:] == '25')
ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 + num2 + num3

    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    u3 = len(str(abs(num3))) == 4

    f1 = u1 + u2 + u3 <= 2
    f2 = summ < maxx
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))

