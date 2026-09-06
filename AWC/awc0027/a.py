n, s, t = map(int, input().split())
a = list(map(int, input().split()))


cnt = 0
for e in a :
    if abs(e-s) <= t : cnt+=1

print(cnt)