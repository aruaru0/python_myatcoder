n = int(input())
a = list(map(int, input().split()))

st = []   # 未解決の人の身長（下から上へ単調非増加）
gp = []   # [その時点の区間最小値, 個数] を st と対応させて保持
ans = 0

for h in a:
    while st and st[-1] < h:
        st.pop()
        ans += gp[-1][0]
        gp[-1][1] -= 1
        if gp[-1][1] == 0:
            gp.pop()
    ac = 0
    while gp and gp[-1][0] > h:
        ac += gp.pop()[1]
    if gp and gp[-1][0] == h:
        gp[-1][1] += ac + 1
    else:
        gp.append([h, ac + 1])
    st.append(h)

print(ans)
