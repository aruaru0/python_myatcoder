s = [input() for _ in range(5)]

ans = 5
for i in range(5) :
    c0, c1 = 0,0
    for j in range(5):
        if s[i][j] == '.' : c0 +=1 
        if s[j][i] == '.' : c1 +=1
    ans = min(ans, c0, c1)

c0, c1 = 0,0
for i in range(5):
    if s[i][i] == '.' : c0 += 1
    if s[i][4-i] == '.' : c1 += 1

ans = min(ans, c0, c1)
print(ans)

