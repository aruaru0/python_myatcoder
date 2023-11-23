n = int(input())

off = ord('a')

node = [[] for _ in range(26)]
for _ in range(n):
    a, b = input().split()
    a = ord(a) - off
    b = ord(b) - off
    node[a].append(b)
    node[b].append(a)



color = [-1 for _ in range(26)]

def dfs(cur, col) :
    color[cur] = col
    for nxt in node[cur] :
        if color[nxt] != -1 : continue
        dfs(nxt, col)


col = 0
for i in range(26):
    if color[i] == -1 :
        dfs(i, col)

    col += 1


s = input()
t = input()

ok = True
for a, b in zip(s, t) :
    a = ord(a) - off
    b = ord(b) - off
    if color[a] != color[b] :
        ok = False

if ok :
    print("Yes")
else:
    print("No")