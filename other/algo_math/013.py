N = int(input())

ans = []
idx = 1

while idx*idx <= N :
    if N%idx == 0 :
        ans.append(idx)
        ans.append(N//idx)

    idx += 1


for e in set(ans):
    print(e)
