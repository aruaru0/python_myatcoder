n = int(input())
a = list(map(int, input().split()))

cnt = 0
tot = sum([a[i-1] < a[i] and a[i] > a[i+1] for i in range(1, n-1)])
print(tot)