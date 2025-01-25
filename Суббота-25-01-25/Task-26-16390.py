with open('26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)

ans_1 = 0
mass = 0
last_box = 0
for box in boxes:
    if mass + box <= S:
        mass += box
        ans_1 += 1
        last_box = box

mass -= last_box
for box in boxes[::-1]:
    if mass + box <= S:
        last_box = box
        break

print(ans_1, last_box)