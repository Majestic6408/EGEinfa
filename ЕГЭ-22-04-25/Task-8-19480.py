from itertools import permutations

a = sorted('ПАРИЖАНКА')
cnt = 0
for val in set(permutations(a)):
    val = ''.join(val)
    val = val.replace('А', 'И')
    if val.count('ИИ') == 1 and 'ИИИ' not in val:
        cnt += 1
print(cnt)