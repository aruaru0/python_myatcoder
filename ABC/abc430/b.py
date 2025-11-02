n, m = map(int, input().split())
s = [input() for _ in range(n)]


st = set()
for i in range(n - m + 1):
    for j in range(n - m + 1):
        sub = ''.join(s[i + d][j:j + m] for d in range(m))
        st.add(sub)

print(len(st))


