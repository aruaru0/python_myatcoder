s = input()


mod = 998244353

def f(s) :
    ret = 0
    for e in s:
        x = ord(e) - ord('0')
        ret = (ret * 10 + x)%mod
    return ret


tot = 1
for e in s.split('*') :
    v = f(e)
    tot *= v
    tot %= mod


print(tot)