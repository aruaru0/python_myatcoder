n, m = map(int, input().split())
s = input()
t = input()


def calc(s, t) :
    ret = 0
    for x, y in zip(s, t) :
        a = ord(x) - ord('0')
        b = ord(y) - ord('0')
        ret += (a-b+10)%10
    return ret

ans = 1e9
for i in range(n-m+1):
    ans = min(ans, calc(s[i:i+m], t))

print(ans)