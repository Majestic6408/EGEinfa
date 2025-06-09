with open('26_21719.txt') as file:
    N = int(file.readline())
    students = {}
    for i in file:
        Id, num = map(int, i.split())
        if Id not in students:
            students[Id] = set()
        students[Id] |= {num}

ans = []
for Id in students:
    student = sorted(students[Id])
    cnt = 1
    max_cnt = 0
    for i in range(len(student) - 1):
        task1, task2 = student[i], student[i + 1]
        if task2 - task1 == 2:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    ans.append([max_cnt, student])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))
print(ans[0])
