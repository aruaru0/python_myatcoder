n, k = map(int, input().split())
a = list(map(int, input().split()))

best = {0: 0}  # 累積和の剰余 -> その剰余での最大 dp
ba = 0         # 全 j での最大 dp
s = 0          # 現在の累積和 mod K
dp = 0
for x in a:
    s = (s + x) % k
    v = ba
    if s in best:
        v = max(v, best[s] + 1)
    dp = v
    if dp > ba:
        ba = dp
    if dp > best.get(s, -1):
        best[s] = dp

print(dp)