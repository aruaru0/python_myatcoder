# Contest ID: abc192
# Problem ID: abc192_d ( https://atcoder.jp/contests/abc192/tasks/abc192_d )
# Title: D. Base n
# Language: Python (3.8.2)
# Submitted: 2021-02-21 01:28:37 +0000 UTC ( https://atcoder.jp/contests/abc192/submissions/20360292 ) 

x = input()
m = int(input())

if len(x) == 1:
    if int(x) <= m:
        print(1)
    else:
        print(0)
    exit()

def f(s, base) :
    ret = 0
    for c in s:
        ret *= base
        ret += int(c)
    return ret

d = int(max(list(x)))

l = d
r = 10**18 + 1

while r - l > 1 :
    mid = (l+r)//2
    if f(x, mid) <= m :
        l = mid
    else :
        r = mid

r -= d + 1
print(r)