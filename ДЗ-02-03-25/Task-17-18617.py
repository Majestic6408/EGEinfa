with open('17_18617.txt') as file:
    data = [int(i) for i in file]

ans = []
maxx = max(i for i in data)
ostat1 = maxx % 3
minn = min(i for i in data)
ostat2 = minn % 7
for i in range(len(data) - 1):
    num1, num2 = data[i:i + 2]
    summ = num1 + num2

    u1 = (num1 % 3) == ostat1
    u2 = (num2 % 3) == ostat1
    f1 = u1 + u2 >= 1

    u3 = (num1 % 7) == ostat2
    u4 = (num2 % 7) == ostat2

    f2 = u3 + u4 >= 1
    if f1 + f2 == 2:
        ans.append(summ)

print(len(ans), max(ans))

