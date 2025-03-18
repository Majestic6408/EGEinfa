ans = []
for n in range(4, 1000):
    st = '>' + '0' * 25 + '1' * n + '2' * 25
    while '>1' in st or '>2' in st or '>0' in st:
        st = st.replace('>1', '22>', 1)
        st = st.replace('>2', '2>', 1)
        st = st.replace('>0', '1>', 1)
    st = st[:-1]
    ans.append([sum(map(int, st)), n])

ans = sorted(ans)
print(ans)

