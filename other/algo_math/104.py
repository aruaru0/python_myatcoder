node = set()
edge = []

level = 1
cur = 1
nxt = []
for i in range(1,5) :
    node.add(cur)
    edge.append([cur, cur+i])
    nxt.append(cur+i)

nxt2 = []
for e in nxt :
    node.add(e)
    for i in range (3):
        edge.append([e, e*3+i])
        nxt2.append(e*3+i)
        node.add(e)
        node.add(e*3+i)

nxt =[]
cnt = 0
for e in nxt2:
    pos = e//3 - 2
    edge.append([e, len(node)+1])
    cnt+=1
    if cnt%3 == 0 : 
        node.add(len(node)+1)
        nxt.append(len(node))

to = len(node)+1
for e in nxt:
    node.add(to)
    edge.append([e, to])

n, m = len(node), len(edge)
print(n, m)
for e in edge :
    print(*e)