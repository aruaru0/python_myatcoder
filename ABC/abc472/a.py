s = input()

t = [ch if ch == 'A' else '.' for ch in s]
print("".join(t))