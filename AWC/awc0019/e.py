import heapq

n = int(input())
bx = []
for _ in range(n):
    w, d = map(int, input().split())
    bx.append((w + d, w, d))
bx.sort()

cum = 0
hp = []
for _, w, d in bx:
    if cum <= d:
        cum += w
        heapq.heappush(hp, -w)
    elif hp and -hp[0] > w and cum + hp[0] <= d:
        cum += w + hp[0]
        heapq.heapreplace(hp, -w)

print(len(hp))
