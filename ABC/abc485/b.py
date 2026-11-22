n, m = map(int, input().split())

s = [input() for _ in range(n)]

for i in range(n) :
    cnt = 0
    for j in range(m) :
        if s[i][j] == 'x' : cnt+=1
    if cnt == m :
        print("Faucet", i+1)
        exit()


for j in range(m) :
    cnt = 0
    for i in range(n) :
        if s[i][j] == 'x' : cnt+=1
    if cnt == n :
        print("Drain", j+1)
        exit()
