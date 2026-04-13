import sys 

sys.setrecursionlimit(10**5)

n = int(input())
l = list(map(int, input().split()))


ans = 0

def dfs(idx, cur, cnt):
    global ans
    if idx == n:
        if cnt > ans:
            ans = cnt
        return
    
    # 1. 負の方向へ進む場合の計算
    v_m = cur - l[idx] * 2
    c_m = 1 if (cur > 0) != (v_m > 0) else 0
    dfs(idx + 1, v_m, cnt + c_m)
    
    # 2. 正の方向へ進む場合の計算
    v_p = cur + l[idx] * 2
    c_p = 1 if (cur > 0) != (v_p > 0) else 0
    dfs(idx + 1, v_p, cnt + c_p)

dfs(0, 1, 0)

# 結果の出力
print(ans)

