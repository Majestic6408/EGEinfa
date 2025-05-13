with open('24_4682.txt') as file:
    data = file.readline()

for i in 'BCD':
    data = data.replace(i, 'C')
for i in 'AE':
    data = data.replace(i, 'A')
data = data.replace('AC', 'L')
for i in'ABCDE':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))