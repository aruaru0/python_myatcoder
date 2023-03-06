# Contest ID: typical90
# Problem ID: typical90_bz ( https://atcoder.jp/contests/typical90/tasks/typical90_bz )
# Title: 078. Easy Graph Problem（★2）
# Language: Python (3.8.2)
# Submitted: 2021-06-28 22:48:06 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/23852230 ) 

N, M = map(int, input().split())

cnt = [0] * N

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    cnt[b] += 1

ans = 0
for i in range(N):
    if cnt[i] == 1:
        ans += 1

print(ans)
