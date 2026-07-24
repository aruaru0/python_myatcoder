N = int(input())
sum = sum(map(int, input().split()))
if sum%N == 0:
    print("Yes")
else:
    print("No")