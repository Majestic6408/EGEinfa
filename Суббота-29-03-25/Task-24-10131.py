with open('24_10131.txt') as file:
    data = file.readline()

pos_A = [i for i in range(len(data)) if data[i] == 'A']

ans = 0
for i in range(1, len(pos_A) - 1):
    for j in range(i, len(pos_A) - 1):
        count_A = j - i + 1
        line = data[pos_A[i - 1] + 1:pos_A[j + 1]]
        count_B = line.count('B')
        if count_A > count_B:
            continue
        while count_A != count_B and (line.find('B') < line.find('A') or line.rfind('A') < line.rfind('B')):
            left_B = line.find('B')
            right_B = len(line) - line.rfind('B')
            if left_B <= right_B:
                line = line[left_B + 1:]
            elif left_B > right_B:
                line = line[:right_B]
            else:
                line = line[left_B + 1:]
            count_B -= 1
        if count_A == count_B:
            ans = max(ans, len(line))