h, w, k = map(int, input().split())
c1, c2 = input().split()

grid = [input() for _ in range(h)]

for i in range(h):
    new_row = ""
    for j in range(w):
        if grid[i][j] == '#':
            new_row += c1 * k
        else:
            new_row += c2 * k
    
    for _ in range(k):
        print(new_row)

