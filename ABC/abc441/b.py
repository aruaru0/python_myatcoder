n, m = map(int, input().split())
s = set(input())
t = set(input())


q = int(input())


for _ in range(q) :
    w = input()

    taka, aoki = True, True
    for e in w:
        if e not in s:
            taka = False
        if e not in t:
            aoki = False

    if taka and not aoki :
        print("Takahashi")
    elif not taka and aoki:
        print("Aoki")
    else:
        print("Unknown")