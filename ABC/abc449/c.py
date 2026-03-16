import bisect

N, L, R = map(int, input().split())
S = input()

POS = [[] for _ in range(26)]
for i, c in enumerate(S):
    POS[ord(c) - ord('a')].append(i)

ans = 0
for PS in POS:
    for i in range(len(PS)):
        low = PS[i] + L
        high = PS[i] + R
        
        left = bisect.bisect_left(PS, low)
        right = bisect.bisect_right(PS, high)
        
        ans += max(0, right - left)

print(ans)
