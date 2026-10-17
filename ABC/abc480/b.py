n, m = map(int, input().split())
s = [input() for _ in range(n)]

def f(x, y) :
    cnt = 0
    for a, b in zip(x, y) :
        if a != b : cnt += 1

    return cnt <= 1


cnt = [0] * n
for _ in range(m) :
    t = input()

    same, near = [],[]
    for idx, e in enumerate(s):
        if len(e) != len(t) :
            continue
        if e == t :
            same.append(idx)
        elif f(e, t) :
            near.append(idx)

    if len(same) == 1 :
        cnt[same[0]] += 1
    elif len(near) == 1 :
        cnt[near[0]] += 1

print(*cnt, sep="\n")