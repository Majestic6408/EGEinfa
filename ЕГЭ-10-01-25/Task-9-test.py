def f1(line):
    return line.count(min(line)) == 1
def f2(line):
    return len(set(line)) != len(line)
def f3(line):
    pov = [i for i in line if line.count(i) != 1]
    return max(line) + min(line) < sum(pov)

with open('input.txt') as file:
    arr = [list(map(int, i.split())) for i in file]

count = 0
for i in arr:
    if all([f1(i), f2(i), f3(i)]):
        count += 1

print(count)
