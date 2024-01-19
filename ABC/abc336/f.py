import hashlib
from collections import deque


def hash(s) :
    sha1 = hashlib.sha1()
    sha1.update(str(s).encode("utf-8"))
    return sha1.hexdigest()

def rot(s, sy, sx) :
    nh, nw = H-1, W-1
    n = (H - 1) * (W - 1) // 2
    cnt = 0
    for y in range(nh):
        for x in range(nw) :    
            s[sy+y][sx+x], s[sy+nh-1-y][sx+nw-1-x] = s[sy+nh-1-y][sx+nw-1-x], s[sy+y][sx+x]
            cnt+=1
            if cnt == n : return s
    return s


H, W = map(int, input().split())

s = [list(map(int, input().split())) for _ in range(H)]
t = [[i*W + j + 1 for j in range(W)] for i in range(H)]

# 最初から一致している場合は探索しない
if t == s : 
    print(0)
    exit()

def BSF() :
    q0 = deque()
    q1 = deque()
    q0.append(s)
    q1.append(t)

    m0 = {hash(s):0}
    m1 = {hash(t):0}


    for i in range(10) :
        tmp0 = deque()
        while len(q0) != 0 :
            cur = q0.popleft()
            cur_h = hash(cur)
            for h in range(2):
                for w in range(2) :
                    tmp = [[cur[j][i] for i in range(W)] for j in range(H)]
                    tmp = rot(tmp, h, w)
                    hval = hash(tmp)
                    if hval in m1 :  # 見つけた場合
                        return m0[cur_h]+m1[hval]+1
                    if hval in m0 :  # 既に登録されている状態の場合はスキップ
                        continue
                    m0[hval] = m0[cur_h] + 1
                    tmp0.append(tmp)
        tmp1 = deque()
        while len(q1) != 0 :
            cur = q1.popleft()
            cur_h = hash(cur)
            for h in range(2):
                for w in range(2) :
                    tmp = [[cur[j][i] for i in range(W)] for j in range(H)]
                    tmp = rot(tmp, h, w)
                    hval = hash(tmp)
                    if hval in m0 :  # 見つけた場合
                        return m0[hval]+m1[cur_h]+1
                    if hval in m1 :  # 既に登録されている状態の場合はスキップ
                        continue
                    m1[hval] = m1[cur_h] + 1
                    tmp1.append(tmp)
        q0, q1 = tmp0, tmp1

    return -1
                    

ret = BSF()
print(ret)
