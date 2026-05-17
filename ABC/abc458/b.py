h, w = map(int, input().split())


for i in range(h):
    for j in range(w):
        cnt = 0
        if i-1 >= 0: cnt+=1
        if j-1 >= 0: cnt+=1
        if i+1 <= h-1: cnt+=1
        if j+1 <= w-1: cnt+=1
        print(cnt, end=" ")
    print()