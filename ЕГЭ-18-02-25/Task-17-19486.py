with open('17_19486.txt') as file:
    data = [int(i) for i in file]

num = [1 for i in data if str(i)[-1:] == '7']
summ1 = sum(map(int, num))
ans = []
cnt = 0
for i in range(len(data) - 1):
    num1, num2 = data[i:i + 2]
    summ = num1 + num2

    u1 = num1 > 0
    u2 = num2 > 0
    u3 = num1 < 0
    u4 = num2 < 0

    if ((u1 and u4) or (u2 and u3)) and summ1 > summ:
        cnt += 1
        ans.append(summ)


print(cnt, max(ans))