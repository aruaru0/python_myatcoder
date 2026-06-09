h, w, k = map(int, input().split())
s = [input() for _ in range(h)]


def f(k : int) ->int :

    if k == -1 : return 0
    res = 0
    for li in range(h):
        a = [0]*w
        for ri in range(li, h):
            for j in range(w): 
                if s[ri][j] == '1' :
                    a[j] += 1

            l, sum = 0,0
            for r in range(w) :
                sum += a[r]
                while sum > k :
                    sum -= a[l]
                    l+=1
                res += r - l + 1

    return res

print(f(k) - f(k-1))
                