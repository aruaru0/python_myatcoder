n, m = map(int, input().split())
es = list(map(int, input().split()))
cs = list(map(int, input().split()))

sc = sum(cs)

me = min(es)

print(me * sc)
