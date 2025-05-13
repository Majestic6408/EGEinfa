with open('24_9845.txt') as file:
    data = file.readline()

for i in 'ABC':
    data = data.replace(i, '*')
for i in '89':
    data = data.replace(i, '&')
while '**' in data or '&&' in data:
    data = data.replace('**', '* *')
    data = data.replace('&&', '& &')

data = data.split()

print(len(max(data, key=len)))