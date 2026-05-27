import sys

M = 998244353
MAX_D = 10**6 + 5

fact = [1] * MAX_D
invFact = [1] * MAX_D

for i in range(1, MAX_D):
    fact[i] = (fact[i-1] * i) % M

invFact[MAX_D-1] = pow(fact[MAX_D-1], M-2, M)
for i in range(MAX_D-2, -1, -1):
    invFact[i] = (invFact[i+1] * (i+1)) % M

def solve():
    N = int(input())
    P = [0] * (N + 1)
    p_line = input().split()
    for i in range(2, N + 1):
        P[i] = int(p_line[i-2])

    C = [0] + list(map(int, input().split()))
    D = [0] + list(map(int, input().split()))

    adj = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        adj[P[i]].append(i)

    # 後序走査の順序生成（再帰制限 avoidance）
    order = []
    stack = [1]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            stack.append(v)
    order.reverse()

    S = [0] * (N + 1)
    K = [0] * (N + 1)
    ans = 1

    for u in order:
        s = C[u]
        k = D[u]
        for v in adj[u]:
            s += S[v]
            k += K[v]
        S[u] = s
        K[u] = k

        if s < k:
            print(0)
            return

        r = D[u]
        n = s - k + r
        num = 1
        for i in range(r):
            num = num * ((n - i) % M) % M
        ways = num * invFact[r] % M
        ans = (ans * ways) % M

    print(ans)

solve()
