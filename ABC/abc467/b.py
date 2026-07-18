n = int(input())

tot = 0
for _ in range(n) :
    e = input().split()
    a, b = int(e[0]), int(e[1])
    s = e[2]
    if s == "keep" :
        tot += b - a


print(tot)