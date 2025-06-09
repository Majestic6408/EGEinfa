from re import *

with open('24-347.txt') as file:
    data = file.readline()

pattern = r'[1-9AB][0-9AB]+'

matches = [i.group() for i in finditer(pattern, data)]
ans = 0
st = 0
for match in matches:
    if int(match, 12) % 3 == 0:
        if ans < len(match):
            ans = len(match)
            st = match
    elif len(match) > ans:
        for l in range(len(match)):
            for r in range(len(match), l, -1):
                sub_str = match[l:r].lstrip('0')
                if sub_str and int(sub_str, 12) % 3 == 0:
                    if ans < len(sub_str):
                        ans = len(sub_str)
                        st = sub_str
                    break
print(ans, data.rfind(st))