from itertools import product

a = sorted(set('МАРКСЛ'))
ans = []
for pos, val in enumerate(product(a, repeat=6), 1):
    val = ''.join(val)
    if val.count('М') == 3 or val.count('А') == 3 or val.count('Р') == 3 or val.count('К') == 3 or val.count('С') == 3 or val.count('Л') == 3:
        val = val.replace('С', '*', 1)
        val = val.replace('К', '<', 1)
        if '*<' not in val and '<*' not in val:
            ans.append(pos)

print(max(ans))