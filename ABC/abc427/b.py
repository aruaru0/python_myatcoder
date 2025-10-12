def digit_sum(x: int) -> int:
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s

N = int(input())

a = 1 
cum = 1

for _ in range(1, N + 1):
    a = cum           # A_i
    fi = digit_sum(a)
    cum += fi

print(a)
