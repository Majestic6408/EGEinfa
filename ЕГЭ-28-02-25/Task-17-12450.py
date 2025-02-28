with open('17_12450.txt') as file:
    data = [int(i) for i in file]

ans = []
minn = min(i for i in data if i % 52 == 0)

for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]

    ostat1 = num1 % 113
    ostat2 = num2 % 113
    ostat3 = num3 % 113
    summ = ostat1 + ostat2 + ostat3
    if summ == minn:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))