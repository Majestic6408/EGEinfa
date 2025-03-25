with open('17_17636.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if len(str(abs(i))) == 3 and str(i)[-1:] == '3')
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    summ = num1 + num2 + num3

    u1 = len(str(abs(num1))) == 3 and str(num1)[-1:] == '3'
    u2 = len(str(abs(num2))) == 3 and str(num2)[-1:] == '3'
    u3 = len(str(abs(num3))) == 3 and str(num3)[-1:] == '3'
    f1 = u1 + u2 + u3 >= 1
    f2 = summ < maxx
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))