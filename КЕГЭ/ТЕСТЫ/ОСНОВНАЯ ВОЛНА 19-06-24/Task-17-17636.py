with open('17_17636.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if len(str(abs(i))) == 3 and str(i)[-1:] == '3')
ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 + num2 + num3

    u1 = str(num1)[-1:] == '3' and len(str(abs(num1))) == 3
    u2 = str(num2)[-1:] == '3' and len(str(abs(num2))) == 3
    u3 = str(num3)[-1:] == '3' and len(str(abs(num3))) == 3
    f1 = u1 + u2 + u3 >= 1
    f2 = summ < maxx
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))