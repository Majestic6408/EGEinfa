with open('17_12249.txt') as file:
    data = [int(i) for i in file]

ans = []
maxx = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-1:] == '3')

for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 + num2 + num3

    u1 = str(num1)[-1:] == '3'
    u2 = str(num2)[-1:] == '3'
    u3 = str(num3)[-1:] == '3'

    f1 = u1 + u2 + u3 >= 1

    if f1 and summ <= maxx:
        ans.append(summ)

print(len(ans), max(ans))