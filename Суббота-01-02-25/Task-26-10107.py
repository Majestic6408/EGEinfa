with open('26_10107.txt') as file:
    N = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1], -x[0]))

cnt = 1
last_event = events[0]
pause = 0
true_events = [events[0]]

for event in events:
    if event[0] >= last_event[1]:
        pause = event[0] - last_event[1]
        last_event = event
        cnt += 1
print(cnt, pause)