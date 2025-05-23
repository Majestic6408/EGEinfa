ans = []
for n in range(101, 10000):
    st = '5' * n
    while '555' in st or '11' in st or '2' in st:
        st = st.replace('555', '1', 1)
        st = st.replace('11', '25', 1)
        st = st.replace('2', '5', 1)
        if int(st) == 15:
           ans.append(n)
           print(min(ans))