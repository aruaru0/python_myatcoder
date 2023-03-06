# Contest ID: abc238
# Problem ID: abc238_c ( https://atcoder.jp/contests/abc238/tasks/abc238_c )
# Title: C. digitnum
# Language: Python (3.8.2)
# Submitted: 2022-05-23 23:18:33 +0000 UTC ( https://atcoder.jp/contests/abc238/submissions/31924350 ) 

N = int(input())

# 現在の桁数の数と、残りの値を返す
def calc(v) :
    s = str(v)
    d = len(s)
    m = 10**(d-1)
    return v-m+1, m-1

mod = 998244353
ans = 0
while N > 0 :
    cnt, nxt = calc(N)
    # 1からcntまでの和は、公式よりcnt * (cnt+1) / 2
    ans += cnt*(cnt+1)//2
    ans %= mod
    N = nxt

print(ans)
