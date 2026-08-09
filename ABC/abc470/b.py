n = int(input()) 
c = list(map(int, input().split()))

cols = [0] * (n+1)
max_col = 0
for e in c:
    cols[e]+=1
    max_col = max(max_col, cols[e])

print(n - max_col)