from itertools import permutations

graph = 'АВ АЗ АЖ ЖД ЖБ БД ВЗ ВГ ГЗ ГД ЗД'.split()

matrix = '256 135 2457 37 1236 157 346'.split()

print(*range(1, 8))
for i in permutations('АБВГДЗЖ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
