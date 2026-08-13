n = int(input())

tot = 0
for _  in range(n-1) :
    a, b = map(int, input().split())
    tot += a
    tot = max(0, tot-b)

tot += int(input())
print(tot)