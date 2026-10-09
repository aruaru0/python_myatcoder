N, M = map(int, input().split())
L = list(map(int, input().split()))
R = list(map(int, input().split()))

L.sort()
R.sort(reverse=True)

# pref[i] = sum of first i (smallest) L values
pref = [0] * (N + 1)
for i in range(N):
    pref[i + 1] = pref[i] + L[i]

# rsum[k] = sum of k largest R values
rsum = [0] * (M + 1)
for k in range(1, M + 1):
    rsum[k] = rsum[k - 1] + R[k - 1]

ok = True
ptr = 0  # number of L values <= k
for k in range(1, M + 1):
    while ptr < N and L[ptr] <= k:
        ptr += 1
    cap = pref[ptr] + k * (N - ptr)
    if rsum[k] > cap:
        ok = False
        break

print("Yes" if ok else "No")
