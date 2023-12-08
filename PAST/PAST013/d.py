N, M = map(int, input().split())
s = input()


cnt = [0 for _ in range(N)]
tbl = 0
for i in range(M):
    n = i%N
    if s[i] == '0' :
        cnt[n] += 1
    elif s[i] == '+':
        cnt[n] += tbl + 1
        tbl = 0
    else :
        tbl += cnt[n] + 1
        cnt[n] = 0

for e in cnt :
    print(e)