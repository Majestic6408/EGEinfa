from re import *

with open('24_20813.txt') as file:
    data = file.readline()

number = r'([7-9][07-9]*|0)'
p = fr'({number}[-*])+{number}'

base = finditer(p, data)
lines = [i.group() for i in base]

print(len(max(lines, key=len)))