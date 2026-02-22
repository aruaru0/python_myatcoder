n, m = map(int, input().split())
x = [(m-a+b-1)//b if a < m else 0 for a, b in [[x for x in list(map(int, input().split()))] for _ in range(n)]]
print(max(x))
