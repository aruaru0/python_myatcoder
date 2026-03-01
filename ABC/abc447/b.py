from collections import defaultdict

s = input()

cnt = defaultdict(int)

mx = -1
for e in s :
    cnt[e]+=1
    mx = max(mx, cnt[e])


t = ""
for e in s :
    if cnt[e] == mx : continue
    t += e


print(t)