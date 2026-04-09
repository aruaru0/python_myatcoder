import typing


class FenwickTree:
    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


n, k = map(int, input().split())

p = list(map(int, input().split()))

def f(k) :
    res, now = 0,0
    bit = FenwickTree(n+1)
    l = 0
    for r in range(n) :
        now += bit.sum(p[r], n+1)
        bit.add(p[r], 1)
        while now > k and l <= r :
            now -= bit.sum(0, p[l])
            bit.add(p[l], -1)
            l += 1
        res += r-l + 1
    return res

print(f(k)-f(k-1))