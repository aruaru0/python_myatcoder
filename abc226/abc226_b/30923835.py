# Contest ID: abc226
# Problem ID: abc226_b ( https://atcoder.jp/contests/abc226/tasks/abc226_b )
# Title: B. Counting Arrays
# Language: Python (3.8.2)
# Submitted: 2022-04-12 04:25:11 +0000 UTC ( https://atcoder.jp/contests/abc226/submissions/30923835 ) 

N = int(input())

def hash(a) :
    hash1, hash2 = 37, 927582227731010101
    ret = hash1
    for e in a :
        ret = (ret * hash1 + e)%hash2
    return ret 

m = set()
for _ in range(N) :
    a = list(map(int, input().split()))
    m.add(hash(a))

print(len(m))