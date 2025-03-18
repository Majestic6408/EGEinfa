with open('17_14952.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(i)[-3:] == '121')
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    summ = num1 + num2 +  num3

    u1 = len(str(abs(num1))) == 4 and num1 % 2 == 0
    u2 = len(str(abs(num2))) == 4 and num2 % 2 == 0
    u3 = len(str(abs(num3))) == 4 and num3 % 2 == 0
    f1 = u1 + u2 + u3 <= 1
    f2 = summ <= maxx
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))