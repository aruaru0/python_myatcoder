# Contest ID: abc173
# Problem ID: abc173_c ( https://atcoder.jp/contests/abc173/tasks/abc173_c )
# Title: C. H and V
# Language: Python (3.8.2)
# Submitted: 2021-12-21 02:05:31 +0000 UTC ( https://atcoder.jp/contests/abc173/submissions/28042482 ) 

H, W, K = map(int, input().split())
c = [input() for _ in range(H)]

def count(h, w) :
    tot = 0
    for y in range(H) :
        for x in range(W) :
            if c[y][x] == '#' :
                if (h>>y)%2 != 1 and (w>>x)%2 != 1 :
                    tot += 1

    return tot


ans = 0
for h in range(1<<H) :
    for w in range(1<<W) :
        ret = count(h, w)
        if ret == K :
            ans+=1

print(ans)
