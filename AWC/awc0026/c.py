n, t, e = map(int, input().split())
p = list(map(int, input().split()))

p.sort()

total, count = 0,0
for v in p :
    if total + v * t <= e :
        total += v*t
        count += 1
    else :
        break

print(count)