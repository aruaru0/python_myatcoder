import sys

def solve():
    n, m = map(int, input().split())

    # aは n+1 のサイズで初期化 (a[n] = 0)
    a = list(map(int, input().split())) + [0]
        
    # 後ろから順に差分を伝搬させる処理
    for i in range(n - 1, -1, -1):
        a[i+1] = (a[i+1] + (m - a[i])) % m
        
    # 左右から足し合わせて半分に縮小する処理
    l_idx, r_idx = 0, n
    while l_idx < r_idx:
        a[l_idx] = (a[l_idx] + a[r_idx]) % m
        l_idx += 1
        r_idx -= 1
        
    new_n = n // 2 + 1
    a = a[:new_n]
    a.sort()
    
    # 答えの計算
    current_l = 0
    current_r = sum(m - val for val in a)
    ans = max(current_l, current_r)
    
    for val in a:
        current_l += val
        current_r -= (m - val)
        res = max(current_l, current_r)
        if res < ans:
            ans = res
                
    print(ans)

T = int(input())
for _ in range(T):
    solve()