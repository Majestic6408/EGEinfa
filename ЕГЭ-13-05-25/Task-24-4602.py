with open('24_4602.txt') as file:
    data = file.readline()

for i in 'BCD':
    data = data.replace(i, 'B')
for i in 'AO':
    data = data.replace(i, 'A')
data = data.replace('BA', 'K')
for i in 'ABCDO':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))