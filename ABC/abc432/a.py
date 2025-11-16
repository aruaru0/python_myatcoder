a, b, c = map(int, input().split())

d = sorted([a, b, c], reverse=True)

ans = int(''.join(map(str, d)))

print(ans)
