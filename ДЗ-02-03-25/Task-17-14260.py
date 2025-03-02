with open('17_14260.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if (i > 0) and len(str(i)) == 4 and str(i)[-1] == str(i)[-2])
ans = []

for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 + num2 + num3

    u1 = len(str(abs(num1))) == 3
    u2 = len(str(abs(num2))) == 3
    u3 = len(str(abs(num3))) == 3

    f1 = u1 + u2 + u3 == 3
    if f1 and summ > minn:
        ans.append(summ)

print(len(ans), max(ans))