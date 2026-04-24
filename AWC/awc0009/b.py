N, S, C = map(int, input().split())
hp = S
fail = 0
for _ in range(N):
    H, P = map(int, input().split())
    if hp >= H:
        hp = hp - H + P
    else:
        fail += 1

print(fail * C)
