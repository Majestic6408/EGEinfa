from re import *
with open('24_6798.txt') as file:
    data = file.readline()

pattern = r'([CDF][CDFAO][AO])+'
matches = finditer(pattern, data)
matches = [match.group() for match in matches]
print(len(max(matches, key=len)) // 3)