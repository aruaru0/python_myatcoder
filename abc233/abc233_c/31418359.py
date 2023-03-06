# Contest ID: abc233
# Problem ID: abc233_c ( https://atcoder.jp/contests/abc233/tasks/abc233_c )
# Title: C. Product
# Language: Python (3.8.2)
# Submitted: 2022-05-03 12:05:54 +0000 UTC ( https://atcoder.jp/contests/abc233/submissions/31418359 ) 

from collections import defaultdict

N, X = map(int, input().split())

p = [[] for _ in range(N)]
for i in range(N) :
    l = list(map(int, input().split()))
    p[i] = l[1:]


x = defaultdict(int)
for e in p[0] :
    x[e]+=1

for i in range(1, N) :
    t = defaultdict(int)
    for e in p[i] :
        for v in x :
            t[e*v] += x[v]
    x,t = t,x

print(x[X])