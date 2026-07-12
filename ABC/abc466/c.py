n = int(input())

r, cnt = 1, 0

for l in range(1, n+1) :
    if l == r : r += 1
    while r <= n :
        print(f"? {l} {r}")
        if input() == "Yes" :
            r += 1
        else : 
            break

    cnt += (r-l-1)

print(f"! {cnt}")