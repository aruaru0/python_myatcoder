import sys
from collections import deque
from array import array

N = int(sys.stdin.readline().strip())

max_states = N * 10
visited = bytearray(max_states)
parent = array('I', [0]) * max_states
SENTINEL = max_states

q = deque()

# 初期状態（1〜9）
for d in range(1, 10):
    rem = d % N
    sid = rem * 10 + d
    if visited[sid]:
        continue
    visited[sid] = 1
    parent[sid] = SENTINEL
    q.append(sid)
    if rem == 0:
        print(d)
        exit()

# BFS
while q:
    cur = q.popleft()
    cur_rem = cur // 10
    last_d   = cur % 10

    for d in range(last_d, 10):
        new_rem = (cur_rem * 10 + d) % N
        new_id  = new_rem * 10 + d
        if visited[new_id]:
            continue
        visited[new_id] = 1
        parent[new_id] = cur

        if new_rem == 0:
            digits = []
            st = new_id
            while True:
                digits.append(str(st % 10))
                if parent[st] == SENTINEL:
                    break
                st = parent[st]
            print(''.join(reversed(digits)))
            exit()


        q.append(new_id)

print(-1)
