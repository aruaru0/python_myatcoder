n = int(input())

for i in range(60):
    if (1<<i)-1 == n: 
        print("Second")
        exit()

print("First")