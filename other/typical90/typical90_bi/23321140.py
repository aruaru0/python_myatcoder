# Contest ID: typical90
# Problem ID: typical90_bi ( https://atcoder.jp/contests/typical90/tasks/typical90_bi )
# Title: 061. Deck（★2）
# Language: Python (3.8.2)
# Submitted: 2021-06-10 02:25:41 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/23321140 ) 

Q = int(input())

a = [0] * (210000)

l = 104999
r = 105000


for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        a[l] = x
        l -= 1
    elif t == 2:
        a[r] = x
        r += 1
    else:
        print(a[l+x])
    # print(a[l+1:r])
