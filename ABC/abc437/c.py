def solve() :
    n = int(input())

    p = []
    totW = 0
    for _ in range(n):
        p.append(list(map(int, input().split())))
        totW += p[-1][0]

    p.sort(key=lambda x: x[0]+x[1], reverse=True)


    totP = 0
    for i in range(n):
        totW -= p[i][0]
        totP += p[i][1]
        if (totW <= totP) :
            print(n - (i+1))
            return
    

t = int(input())

for _ in range(t):
    solve()