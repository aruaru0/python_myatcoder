import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

n = len(s)
m = len(t)

f = [float('inf')] * n

def get_after(char, start_n):
    after_c = [float('inf')] * (start_n + 1)
    for i in range(start_n - 1, -1, -1):
        if s[i] == char:
            after_c[i] = i
        else:
            after_c[i] = after_c[i+1]
    return after_c

after_t0 = get_after(t[0], n)
for i in range(n):
    f[i] = after_t0[i]
    
for k in range(1, m):
    char_k = t[k]
    after_ck = get_after(char_k, n)
    new_f = [float('inf')] * n
    for i in range(n):
        prev_end = f[i]
        if prev_end == float('inf'):
            continue
        next_idx = prev_end + 1
        if next_idx < n:
            new_f[i] = after_ck[next_idx]
        else:
            new_f[i] = float('inf')
    f = new_f

total_sub = n * (n + 1) // 2

bad_sub = 0
for i in range(n):
    if f[i] != float('inf'):
        bad_sub += (n - f[i])
        
print(total_sub - bad_sub)
