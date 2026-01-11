n = int(input())
p = [[v, i+1] for i, v in enumerate(list(map(int, input().split())))]
p.sort()

for e in p[:3]:
    print(e[1], end=' ')

print()