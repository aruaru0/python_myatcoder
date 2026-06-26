n, k = map(int, input().split())

result = 0
for _ in range (n):
    c, d = map(int, input().split())
    if c <= k :
        result += d
    
print(result)