N = int(input())
v = list(map(int, input().split()))
v.sort()

tot = sum([v[i] - v[i-1] for i in range(1, N)])

print(tot)