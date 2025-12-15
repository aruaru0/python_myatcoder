n, m = map(int, input().split())

s = set()

cnt = 0
for _ in range(m) :
    r,c = map(int, input().split())
    if (r,c) not in s and (r+1,c) not in s and (r,c+1) not in s and (r+1,c+1) not in s :
        cnt += 1
        s.add((r,c))
        s.add((r+1,c))
        s.add((r,c+1))
        s.add((r+1,c+1))
print(cnt)