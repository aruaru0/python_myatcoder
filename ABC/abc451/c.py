import heapq

q = int(input())

pq = []

for _ in range(q) :
    t, h = map(int, input().split())

    if t == 1 :
        heapq.heappush(pq, h)
    else :
        while len(pq) != 0 and pq[0] <= h :
            heapq.heappop(pq)

    print(len(pq))