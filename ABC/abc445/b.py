n = int(input())
s = [input() for _ in range(n)]

m = max(map(len, s))

for e in s :
    d = (m - len(e))//2
    print("."*d + e + "."*d)