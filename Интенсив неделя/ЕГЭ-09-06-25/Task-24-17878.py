from re import *

with open('24_17878.txt') as file:
    data = file.readline()

number = r'([1-9][0-9]*|0)'

pattern = fr'({number}[-*])+{number}'

matches = [i.group() for i in finditer(pattern, data)]

print(len(max(matches, key=len)))