ans = []
for n in range(4, 10000):
    st = '8' + '4' * n
    while '11' in st or '444' in st or '8888' in st:
        st = st.replace('11', '4', 1)
        st = st.replace('444', '88', 1)
        st = st.replace('8888', '1', 1)
    summ = sum(map(int, st))
    ans.append(summ)

print(max(ans))