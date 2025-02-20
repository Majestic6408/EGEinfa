with open('17.txt') as file:
    data = [int(i) for i in file]

ans = []
maxx = max(i for i in data if str(i)[-2:] == '50')

for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 + num2 + num3

    u1 = (num1 != num2) and (num2 != num3) and (num1 != num3)
    u2 = len(str(abs(num1))) == 5 and len(str(abs(num2))) == 5 and len(str(abs(num3))) == 5
    f1 = u1 + u2 >= 1

    if f1 >= 1 and summ <= maxx:
        ans.append(summ)

print(len(ans), max(ans))


