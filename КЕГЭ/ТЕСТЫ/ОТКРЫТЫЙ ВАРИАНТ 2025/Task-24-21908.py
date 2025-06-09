from re import *

with open('24_21908.txt') as file:
    data = file.readline()

pattern = r'[1-9ABCD][0-9ABCD]*[02468AC]+'

matches = [i.group() for i in finditer(pattern, data)]

print(len(max(matches, key=len)))