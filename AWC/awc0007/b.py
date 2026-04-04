n, k = map(int, input().split())

lst = []
for _ in range(n):
    mv = int(input())
    tms = set(input().split())
    lst.append(tms)
    
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if len(lst[i] & lst[j]) >= k:
            cnt += 1

print(cnt)

