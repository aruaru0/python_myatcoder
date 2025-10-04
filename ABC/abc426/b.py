from collections import defaultdict


s = input().strip()
cnt = defaultdict(int)
for c in s:
    cnt[c] += 1

for c in s:
    if cnt[c] == 1:
        print(c)

