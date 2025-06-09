from atcoder import dsu

# 入力
n = int(input())
p = [(x-1, y-1, i) for i, (x, y) in enumerate(map(int, input().split()) for _ in range(n))]
p.sort()

# Union-Find木の初期化
uf = dsu.DSU(n)
# スタック
stack = []

# スタックを使って、x座標が小さい順にy座標を比較
for x,y,i in p:
    loc = -1

    if stack:
        while (loc + len(stack)) >= 0:
            if stack[loc][1] > y:
                break
            else:
                # スタックの要素を比較して、y座標が小さいものを見つける
                uf.merge(stack[loc][2], i)
                loc -= 1
    
    if loc == -1:
        stack.append((x,y,i))
    
for i in range(n):
    print(uf.size(i))
