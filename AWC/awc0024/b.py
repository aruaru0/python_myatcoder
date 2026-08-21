from atcoder import dsu

n,m,k = map(int,input().split())

s = [False] * n
for i in range(k) :
    s[i] = True

for _ in range(m) :
    a, b = map(int, input().split())
    a-=1
    b-=1
    s[a] = s[b] = s[a] | s[b]

print(sum(s))
