import sys
from bisect import bisect_left

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

INF = 3 * 10**10
A.append(INF)

results = []

for _ in range(Q):
    X, Y = map(int, input().split())
    
    idx_start = bisect_left(A, X)
    
    low = idx_start
    high = len(A) - 1
    k = high 
    
    while low <= high:
        mid = (low + high) // 2
        
        missing_cnt = (A[mid] - X) - (mid - idx_start)
        
        if missing_cnt >= Y:
            k = mid
            high = mid - 1
        else:
            low = mid + 1
    
    ans = (X + Y - 1) + (k - idx_start)
    results.append(ans)

# 結果をまとめて出力
print('\n'.join(map(str, results)))
