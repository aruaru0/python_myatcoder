import sys
import heapq

sys.setrecursionlimit(2000)

input = sys.stdin.read
data = input().split()

iterator = iter(data)
N = int(next(iterator))
K = int(next(iterator))
X = int(next(iterator))

A = []
for _ in range(N):
    A.append(int(next(iterator)))

A.sort(reverse=True)

max_base_sum = K * A[0]

D = []
for i in range(1, N):
    D.append(A[0] - A[i])

results = []

pq = []

results.append(max_base_sum)

if N == 1:
    for res in results:
        print(res)
    exit()

heapq.heappush(pq, (D[0], 0, 1))

while len(results) < X:
    if not pq:
        break
        
    cost, last_idx, count = heapq.heappop(pq)
    
    results.append(max_base_sum - cost)
    
    if count + 1 <= K:
        heapq.heappush(pq, (cost + D[last_idx], last_idx, count + 1))
        
    if last_idx + 1 < len(D):
        new_cost = cost - D[last_idx] + D[last_idx + 1]
        heapq.heappush(pq, (new_cost, last_idx + 1, count))

for res in results:
    print(res)
