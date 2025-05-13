with open('24_7600.txt') as file:
    data = file.readline()

for i in 'QRS':
    data = data.replace(i, '(')
while '((' in data:
    data = data.replace('((', '( (')

data = data.split()
print(len(max(data, key=len)))