import sys
sys.setrecursionlimit(10**6)

line = input().split()
n, m = int(line[0]), int(line[1])

cars = []
for i in range(m):
    lr = list(map(int, input().split()))
    l, r = lr[0], lr[1]
    cars.append((l, r))

# 右端でソート（等しければ左端でも）
cars.sort(key=lambda x: (x[1], x[0]))

# Union-Find構造：next_free[i] は i 以降の最初空きスペース
next_free = list(range(n + 2))

def find(i):
    if next_free[i] != i:
        next_free[i] = find(next_free[i])
    return next_free[i]

for l, r in cars:
    pos = find(l)
    
    # 空きスペースが範囲内にあるか確認
    if pos > r:
        print("No")
        exit()
    
    # このスペースを使用済みとして次の空をリンク
    next_free[pos] = find(pos + 1)

print("Yes")
