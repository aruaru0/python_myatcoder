n = int(input())
q = list(map(int, input().split()))
mod = 998244353

ans = 1
st = []  
for i in range(n):
    v = q[i]
    while st and q[st[-1]] < v:
        st.pop()
    if i >= 1:
        c = i - st[-1] if st else i
        ans = ans * c % mod
    st.append(i)

print(ans)
