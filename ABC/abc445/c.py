N = int(input())
a = [0] + list(map(int, input().split()))
res = [0]*(N+1)

for i in range(N, 0, -1):
    if a[i] == i:
        res[i] = i
    else:
        res[i] = res[a[i]] 

print(' '.join(map(str, res[1:])))
