N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

tot = 0
for i in range(N):
    tot += abs(a[i] - b[i])

print(tot)