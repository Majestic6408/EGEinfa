from itertools import product
from string import digits, ascii_uppercase

a = digits + ascii_uppercase
a = a[:16]
cnt = 0
for val in product(a, repeat=3):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) == 3:
        val = val.replace('2', '*', 1).replace('4', '*', 1).replace('6', '*', 1).replace('8', '*', 1).replace('A', '*', 1).replace('C', '*', 1).replace('E', '*', 1).replace('G', '*', 1).replace('0', '*', 1)
        val = val.replace('1', '<', 1).replace('3', '<', 1).replace('5', '<', 1).replace('7', '<', 1).replace('9', '<', 1).replace('B', '<', 1).replace('D', '<', 1).replace('F', '<', 1)
        if '<<' not in val and '**' not in val:
            cnt +=1

print(cnt)