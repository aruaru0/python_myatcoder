T = int(input())
ans = []

def check(s):
    ret = []
    for c in s:
        if len(ret) >= 3 and ret[-3] == '(' and ret[-2] == 'x' and ret[-1] == 'x' and c == ')':
            ret.pop()
            ret.pop()
            ret.pop()
            ret.append('x')
            ret.append('x')
        else:
            ret.append(c)
    return ret



for _ in range(T):
    A = input()
    B = input()

    if check(A) == check(B):
        ans.append("Yes")
    else:
        ans.append("No")

print('\n'.join(ans))

