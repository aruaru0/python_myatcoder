# Contest ID: typical90
# Problem ID: typical90_bx ( https://atcoder.jp/contests/typical90/tasks/typical90_bx )
# Title: 076. Cake Cut（★3）
# Language: Python (3.8.2)
# Submitted: 2021-06-27 23:39:49 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/23834524 ) 

N = int(input())
a = list(map(int, input().split()))
tot = sum(a)

if tot % 10 != 0:
    print("No")
    exit(0)

tot //= 10
a = a + a
n = len(a)

sum = 0
l, r = 0, 0
ok = False
while r < n:
    while r < n and sum < tot:
        sum += a[r]
        r += 1
    if tot == sum:
        ok = True
        break
    while l < n and sum > tot:
        sum -= a[l]
        l += 1
    if tot == sum:
        ok = True
        break

if ok:
    print("Yes")
else:
    print("No")
