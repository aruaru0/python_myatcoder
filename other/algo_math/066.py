n, k = map(int, input().split())

diff = k - 1
tot = 0
for a in range(1, n+1) :
    for b in range(max(1, a-diff), min(n, a+diff)+1):
        for c in range(max(1, a-diff), min(n, a+diff)+1):
            if abs(b-c) < k : tot += 1

print(n**3 - tot)

