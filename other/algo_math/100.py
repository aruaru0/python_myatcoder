import numpy as np

Q = int(input())

def powMatrix(A: np.array , p :int) ->np.array :
    
    ret = np.eye(A.shape[0])
    while p > 0 :
        if p&1 == 1:
            ret = np.matmul(ret, A)
        A = np.matmul(A, A)
        p >>= 1
    return ret

for _ in range(Q):
    x, y, z, t = input().split()
    x = float(x)
    y = float(y)
    z = float(z)
    t = int(t)
    a = np.array([[1-x, y, 0],[0, 1-y, z], [x, 0, 1-z]])
    res = powMatrix(a, t)
    print(*res.sum(axis=1))

    