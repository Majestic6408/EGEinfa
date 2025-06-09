with open('17_21712.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i > 0 and len(str(abs(i))) == 4 and str(i)[-1] == '6')

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    summ = num1 + num2 + num3

    u1 = len(str(abs(num1))) == 4 and str(num1)[-1] == '6'
    u2 = len(str(abs(num2))) == 4 and str(num2)[-1] == '6'
    u3 = len(str(abs(num3))) == 4 and str(num3)[-1] == '6'
    f1 = u1 + u2 + u3 == 1
    f2 = summ <= minn
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))
