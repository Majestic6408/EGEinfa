with open('26_21910.txt') as file:
    N = file.readline()
    data = [int(i) for i in file]

boxes = sorted(data)[::-1]
cnt = 1
last_box = boxes[0]

for box in boxes:
    if last_box - box >= 9:
        cnt += 1
        last_box = box

print(cnt, last_box)
