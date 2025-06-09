from re import *
from string import *

with open('24_17685.txt') as file:
    data = file.readline()

number = r'([1-9][0-9]*|0)'
pattern = fr'({number}[+*])+{number}'

matches = [i.group() for i in finditer(pattern, data)]

ans = 0
for match in matches:
    if eval(match) == 0:
        ans = max(ans, len(match))
    elif len(match) > ans:
        for l in range(len(match)):
            for r in range(len(match), l, -1):
                sub_str = match[l:r].strip('+*')
                if len(sub_str) < 2 or sub_str[0] == '0' and sub_str[1] in digits:
                    break
                if eval(sub_str) == 0:
                    ans = max(ans, len(sub_str))
                    break

print(ans)