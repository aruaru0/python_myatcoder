from collections import defaultdict

n, q = map(int, input().split())

mp = defaultdict(int)
cur = 0
for _ in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1 :
        cur ^= mp[t[1]]
        mp[t[1]] += 1
        cur ^= mp[t[1]]
    else :
        cur = 0
        zero = []
        for e in mp.keys() :
            mp[e]-=1
            cur ^= mp[e]
            if mp[e] == 0 :
                zero.append(e)
        for e in zero :
            del mp[e]

    print(cur)

        