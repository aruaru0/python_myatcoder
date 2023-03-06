# Contest ID: abc226
# Problem ID: abc226_b ( https://atcoder.jp/contests/abc226/tasks/abc226_b )
# Title: B. Counting Arrays
# Language: Python (3.8.2)
# Submitted: 2022-04-11 23:50:55 +0000 UTC ( https://atcoder.jp/contests/abc226/submissions/30920793 ) 

N = int(input())

m = set()
for _ in range(N) :
    x = tuple(map(int, input().split()))
    m.add(x)

print(len(m))