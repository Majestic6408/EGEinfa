with open('26_21424.txt') as file:
    N = file.readline()
    data = [int(i) for i in file]

boxes = sorted(data, reverse=True)

last_boxes = boxes[0]
cnt = 1
for box in boxes:
    if last_boxes - box >= 9:
        cnt += 1
        last_boxes = box

print(cnt, last_boxes)