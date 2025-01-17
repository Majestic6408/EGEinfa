from itertools import permutations

graph = 'BC BD BE DE DG CH EH HF FA FG GA'.split()

matrix = '234 157 147 138 268 58 23 456'.split()

print(*range(1, 9))
for i in permutations('ABDCEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
