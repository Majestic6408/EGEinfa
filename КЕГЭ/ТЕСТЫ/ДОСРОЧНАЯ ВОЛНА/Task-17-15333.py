with open('17_15333.txt') as file:
    data = [int(i) for i in file]

ans = []
maxx = max(i for i in data if i % 19 == 0)
for i in range(len(data) - 1):
    num1, num2 = data[i:i + 2]
    summ = num1 + num2

    u1 = num1 > maxx
    u2 = num2 > maxx
    f = u1 + u2 >= 1
    if f:
        ans.append(summ)

print(len(ans), max(ans))