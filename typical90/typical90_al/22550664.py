# Contest ID: typical90
# Problem ID: typical90_al ( https://atcoder.jp/contests/typical90/tasks/typical90_al )
# Title: 038. Large LCM（★3）
# Language: Python (3.8.2)
# Submitted: 2021-05-13 04:07:04 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/22550664 ) 

a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a//gcd(a, b) * b


if lcm(a, b) > 10**18:
    print("Large")
else:
    print(lcm(a, b))
