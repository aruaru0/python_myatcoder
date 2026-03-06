n,k = map(int, input().split())

p = [list(map(int, input().split())) for _ in range(n)]

p.sort(key=lambda x: x[0]-x[1], reverse=True)

tot = sum([x[0] for x in p])

for i in range(k) :
    tot -= p[i][0] - p[i][1]

print(tot)

