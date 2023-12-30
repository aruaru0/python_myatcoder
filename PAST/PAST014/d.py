h, a, b, c, d = list(map(int, input().split()))


ans = (h + a - 1)//a * b
tot = 0
while h > 0 :
    # print(ans, h, tot, end = "->")
    h -= c
    h -= h//2
    tot += d
    # print(h, (h+a-1)//a * b)
    if h <= 0: ans = min(ans, tot)
    else: ans = min(ans, tot + (h+a-1)//a * b)


print(ans)